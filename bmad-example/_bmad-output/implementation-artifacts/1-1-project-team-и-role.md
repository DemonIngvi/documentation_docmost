---
title: 'Project, Team и Role'
type: 'feature'
created: '2026-11-01'
status: 'done'
route: 'dispatch'
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/planning-artifacts/architecture/architecture-bmad-example-2026-11-01/ARCHITECTURE-SPINE.md'
---

> Учебный пример: реализация смоделирована, код не написан. Записи о тестах и ревью показывают форму документа, это не результаты реальных запусков.

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** В Векторе нет каркаса приложения и способа завести Project с правами.

**Approach:** Создать каркас из архитектуры, модуль `access` и управление Project, Team и Role. Покрывает FR-1 и FR-2.

## Boundaries & Constraints

**Always:** Каждый запрос чтения получает `ProjectScope` (AD-7). Чужой Project даёт 404, нехватка Role даёт 403.

**Never:** Не делать единый вход через внешние каталоги, это не входит в историю.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| S1 Создание Project | Administrator, Process выбран | Project создан | N/A |
| S3 Нет Process | Запрос без Process | Project не создан | 422 с причиной |
| S5 Нет Role | Пользователь без Role читает Work Item | Данные скрыты | 404 |
| S5 Observer меняет | Role Observer | Изменение отклонено | 403 |

**Not applicable:** S2 — другой допустимой ветки создания Project нет; S4 — в FR-1 и FR-2 нет числовых лимитов; S6 — история не вызывает внешних систем; S7, S8 — повторное создание защищено уникальным именем Project; S9 — у истории нет настроек поведения; S10 — каждая операция выполняется одной транзакцией; S11 — удаление Project в историю не входит; S12 — аудит изменений Role отложен вместе с журналом

</frozen-after-approval>

## Code Map

- `deploy/docker-compose.yml` -- все службы
- `apps/api/src/modules/access/` -- Project, Team, Role, `ProjectScope`

## Tasks & Acceptance

**Execution:**
- [x] `deploy/docker-compose.yml` -- описать службы -- NFR-4
- [x] `apps/api/src/modules/access/domain/` -- правила Role -- AD-7
- [x] `apps/api/src/modules/access/adapters/` -- REST и БД -- FR-1, FR-2
- [x] `apps/api/test/access.e2e.ts` -- проверить строки матрицы -- граничные случаи

**Acceptance Criteria:**
- Given чистый сервер, when выполнен `docker compose up`, then приложение открывается и Administrator может войти.

## Implementation Notes

- Смоделировано: `ProjectScope` сделан обязательным параметром типа, чтобы правило AD-7 проверялось при компиляции.

## Spec Change Log

## Review Triage Log

| Находка | Вердикт | Обоснование |
|---------|---------|-------------|
| Ответ 404 отличается по времени от 403 | low | Смоделировано: принято, риск перебора мал |

## Verification

**Commands:**
- `pnpm test --filter access` -- expected: все тесты зелёные
