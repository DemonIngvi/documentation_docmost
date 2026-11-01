"""Публикует пример BMAD в Docmost. Повторный запуск заменяет страницы пространства."""
import http.cookiejar
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
import uuid

BASE = "http://127.0.0.1:3100"
CRED = pathlib.Path(r"D:\documentation\docmost\admin-credentials.txt")
ROOT = pathlib.Path(r"D:\documentation\bmad-example")
OUT = "_bmad-output/"
PLAN = OUT + "planning-artifacts/"
IMPL = OUT + "implementation-artifacts/"
SPACE_NAME, SPACE_SLUG = "Вектор: пример BMAD", "vektor-bmad"

TREE = [
    ("Как читать этот пример", "docs/index.md", []),
    ("1. Анализ", None, [
        ("Итог брейншторма", OUT + "brainstorming/brainstorming-ai-tracker-2026-11-01/brainstorm-intent.md"),
        ("Исследование модели Targetprocess", PLAN + "research/competitive-targetprocess-model-2026-11-01/research.md"),
        ("Product Brief", PLAN + "briefs/brief-bmad-example-2026-11-01/brief.md"),
        ("PRFAQ", PLAN + "prfaq-bmad-example.md"),
    ]),
    ("2. Планирование", None, [
        ("PRD", PLAN + "prds/prd-bmad-example-2026-11-01/prd.md"),
        ("Дополнение к PRD", PLAN + "prds/prd-bmad-example-2026-11-01/addendum.md"),
        ("UX: DESIGN", PLAN + "ux-designs/ux-bmad-example-2026-11-01/DESIGN.md"),
        ("UX: EXPERIENCE", PLAN + "ux-designs/ux-bmad-example-2026-11-01/EXPERIENCE.md"),
    ]),
    ("3. Решения", None, [
        ("Architecture Spine", PLAN + "architecture/architecture-bmad-example-2026-11-01/ARCHITECTURE-SPINE.md"),
        ("Эпики и истории", PLAN + "epics.md"),
        ("Проверка готовности", PLAN + "implementation-readiness.md"),
    ]),
    ("4. Реализация", None, [
        ("Статус спринта", IMPL + "sprint-status.yaml"),
        ("История 1.1: Project, Team и Role", IMPL + "1-1-project-team-и-role.md"),
        ("История 1.2: Иерархия Work Item и Bug", IMPL + "1-2-иерархия-work-item-и-bug.md"),
        ("История 1.3: Process и Workflow", IMPL + "1-3-process-и-workflow.md"),
        ("Сводка автотестов", IMPL + "tests/test-summary.md"),
        ("Sprint Change Proposal", PLAN + "sprint-change-proposal-2026-11-01.md"),
        ("Ретроспектива Эпика 1", IMPL + "epic-1-retro-2026-11-01.md"),
    ]),
    ("Контекст проекта", "AGENTS.md", []),
]

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))


def post(path, data=None, raw=None, ctype="application/json"):
    body = raw if raw is not None else json.dumps(data or {}).encode()
    req = urllib.request.Request(BASE + path, data=body, headers={"Content-Type": ctype}, method="POST")
    try:
        with opener.open(req, timeout=60) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{path}: {e.code} {e.read()[:400]!r}")


def prepare(title, source):
    if source is None:
        return f"# {title}\n\nДокументы этой фазы находятся на вложенных страницах.\n"
    text = (ROOT / source).read_text(encoding="utf-8")
    if source.endswith(".yaml"):
        comment = "> Файл создан и обновлён штатными скриптами BMAD. Статусы Эпика 1 смоделированы: код не писался."
        return f"# {title}\n\n{comment}\n\n```yaml\n{text}\n```\n"
    meta = ""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        meta = f"\n\n## Метаданные документа\n\n```yaml\n{m.group(1)}\n```\n"
        text = text[m.end():]
    text = re.sub(r"<!--.*?-->\n?", "", text, flags=re.S)
    text = re.sub(r"</?frozen-after-approval[^>]*>\n?", "", text)
    text = re.sub(r"^\s*# .*\n", "", text, count=1)
    return f"# {title}\n\n{text.strip()}\n{meta}"


def import_page(space_id, content):
    bd = uuid.uuid4().hex
    body = (
        f'--{bd}\r\nContent-Disposition: form-data; name="spaceId"\r\n\r\n{space_id}\r\n'
        f'--{bd}\r\nContent-Disposition: form-data; name="file"; filename="page.md"\r\nContent-Type: text/markdown\r\n\r\n'
    ).encode() + content.encode("utf-8") + f"\r\n--{bd}--\r\n".encode()
    return post("/api/pages/import", raw=body, ctype=f"multipart/form-data; boundary={bd}")["data"]["id"]


cred = dict(line.split(": ", 1) for line in CRED.read_text(encoding="utf-8").splitlines())
post("/api/auth/login", {"email": cred["email"], "password": cred["password"]})

spaces = post("/api/spaces", {"limit": 100})["data"]["items"]
space = next((s for s in spaces if s["slug"] == SPACE_SLUG), None)
if space is None:
    space = post("/api/spaces/create", {"name": SPACE_NAME, "slug": SPACE_SLUG,
                                        "description": "Полный учебный пример документации BMAD"})["data"]
space_id = space["id"]

old = post("/api/pages/sidebar-pages", {"spaceId": space_id, "limit": 100})["data"]["items"]
for page in old:
    post("/api/pages/delete", {"pageId": page["id"], "permanentlyDelete": True})

count = 0
errors = []
for i, (title, source, children) in enumerate(TREE):
    pid = import_page(space_id, prepare(title, source))
    post("/api/pages/move", {"pageId": pid, "parentPageId": None, "position": f"a{i:04d}"})
    count += 1
    for j, (child_title, child_source) in enumerate(children):
        content = prepare(child_title, child_source)
        cid = import_page(space_id, content)
        post("/api/pages/move", {"pageId": cid, "parentPageId": pid, "position": f"a{j:04d}"})
        count += 1
        saved = post("/api/pages/info", {"pageId": cid, "format": "markdown"})["data"]["content"]
        if len(saved) < 0.7 * len(content) or content.count("```mermaid") != saved.count("```mermaid"):
            errors.append(f"{child_title}: {len(content)} -> {len(saved)}")

roots = post("/api/pages/sidebar-pages", {"spaceId": space_id, "limit": 100})["data"]["items"]
print(f"Опубликовано страниц: {count}, корневых: {len(roots)}")
print(f"Открыть: http://localhost:3100/s/{SPACE_SLUG}")
print("\n".join(errors) if errors else "Содержимое сохранилось")
sys.exit(1 if errors else 0)
