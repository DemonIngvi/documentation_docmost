"""Создаёт журналы решений (.memlog.md) и записывает ретроспективу штатными скриптами BMAD."""
import json
import os
import pathlib
import subprocess

ROOT = pathlib.Path(r"D:\documentation\bmad-example")
MEMLOG = ROOT / "_bmad/scripts/memlog.py"
IMPL = ROOT / "_bmad-output/implementation-artifacts"
ENV = {**os.environ, "PYTHONUTF8": "1"}

RUNS = {
    "_bmad-output/brainstorming/brainstorming-ai-tracker-2026-11-01": ("AI-трекер работы", [
        ("decision", "Выбран принцип: ИИ предлагает, человек применяет. Причина: pre-mortem показал потерю доверия."),
        ("event", "Учебный пример: сессия проведена в режиме Ideate for me."),
    ]),
    "_bmad-output/planning-artifacts/briefs/brief-bmad-example-2026-11-01": ("Вектор", [
        ("decision", "Поставка в контуре компании, потому что целевым клиентам нужен контроль над данными."),
    ]),
    "_bmad-output/planning-artifacts/prds/prd-bmad-example-2026-11-01": ("Вектор", [
        ("decision", "Режим Fast path: это учебный пример, человек не участвовал в выводах."),
        ("assumption", "Размер компании от 20 до 200 разработчиков, в примере не подтверждено."),
        ("change", "FR-16 расширен локальной моделью по Sprint Change Proposal."),
    ]),
    "_bmad-output/planning-artifacts/ux-designs/ux-bmad-example-2026-11-01": ("Вектор", [
        ("decision", "Весь контент ИИ выделен отдельным цветом и подписью, чтобы отличать предложение от данных."),
    ]),
    "_bmad-output/planning-artifacts/architecture/architecture-bmad-example-2026-11-01": ("Вектор", [
        ("decision", "Модульный монолит вместо микросервисов: целевой размер не требует независимого масштабирования."),
        ("decision", "AI Suggestion хранится отдельно, чтобы правило подтверждения обеспечивала структура данных."),
        ("assumption", "Конкретная модель не выбрана, скрыта портом ModelProvider."),
    ]),
}


def run(*args):
    r = subprocess.run(["uv", "run", "--no-cache", *map(str, args)], cwd=ROOT, env=ENV, capture_output=True, encoding="utf-8")
    if r.returncode:
        raise SystemExit(f"{args}: {r.stdout}{r.stderr}")
    return r.stdout.strip()


for rel, (topic, entries) in RUNS.items():
    ws = ROOT / rel
    if (ws / ".memlog.md").exists():
        continue
    run(MEMLOG, "init", "--workspace", ws, "--field", f"topic={topic}")
    for kind, text in entries:
        run(MEMLOG, "append", "--workspace", ws, "--type", kind, "--text", text)
    print("memlog", ws.name)

actions = [
    {"action": "Добавлять проверку циклов в матрицы историй со связями", "owner": "Дима"},
    {"action": "Спрашивать о требованиях безопасности на первой встрече", "owner": "Лина"},
    {"action": "Подготовить стенд для NFR-1 до истории 2.1", "owner": "Павел"},
]
status = IMPL / "sprint-status.yaml"
if "action_items:" not in status.read_text(encoding="utf-8"):
    print(run(
        ROOT / ".claude/skills/bmad-retrospective/scripts/sprint_status.py", "update",
        "--file", status, "--epic", "1", "--set-retro-done",
        "--add-action", json.dumps(actions, ensure_ascii=False),
        "--ref", IMPL / "epic-1-retro-2026-11-01.md",
        "--verdict", "accepted-with-open-items", "--date", "11-01-2026 10:30",
    ))
print(run(ROOT / ".claude/skills/bmad-sprint-planning/scripts/sprint_plan.py", "validate", "--status-file", status))
