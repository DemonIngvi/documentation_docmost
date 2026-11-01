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

**Approach:** Создать каркас из архитектуры, модуль `access` и управление Project, Team и Role. Покрывает FR-1, FR-2 и FR-23.

## Boundaries & Constraints

**Always:** Каждый запрос чтения получает `ProjectScope` (AD-7), он строится из пользователя сессии и `project_id` в пути. Чужой Project даёт 404, нехватка Role даёт 403. Вход и токены устроены по AD-12. Process для теста создаётся заранее: список Process заполняет история 1.3, до неё берётся Process по умолчанию из миграции. Поля Project: `name` от 1 до 100 символов, `process_id`, `program_id` необязателен. Ошибки по RFC 9457. Team не даёт прав.

**Never:** Не делать единый вход через внешние каталоги, это не входит в историю.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| S1 Создание Project | Administrator, Process выбран | Project создан | N/A |
| S3 Нет Process | `POST /projects` без `process_id` | Project не создан | 422, code `process_required` |
| S3 Несуществующий Process | `process_id` не найден | Project не создан | 422, code `process_not_found` |
| S3, S7, S8 Дубль имени | Имя занято в Program, в том числе параллельным запросом | Project не создан | 409, code `project_name_taken` |
| S1 Создание Team и назначение Role | Administrator задаёт Team и Role пользователя | Role действует со следующего запроса | N/A |
| S1 Первый вход | Заданы `ADMIN_EMAIL`, `ADMIN_PASSWORD`, пользователей нет | Administrator создан и вошёл | N/A |
| S3 Неверный пароль | Почта есть, пароль неверен | Вход отклонён | 401, code `invalid_credentials` |
| S10 Отключённый пользователь | Сессия или токен отключённого пользователя | Запрос отклонён | 401, code `invalid_credentials` |
| S5 Нет Role | Пользователь без Role в Project читает `GET /projects/{id}` | Project считается чужим, данные скрыты | 404 |
| S5 Observer меняет | Role Observer меняет Project | Изменение отклонено | 403 |

**Not applicable:** S2 — другой допустимой ветки создания Project нет; S4 — в FR-1 и FR-2 нет числовых лимитов; S6 — история не вызывает внешних систем; S9 — у истории нет настроек поведения; S11 — удаление Project в историю не входит; S12 — аудит изменений Role отложен вместе с журналом

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
