---
title: 'Process и Workflow'
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

**Problem:** Work Item нельзя вести по процессу команды.

**Approach:** Модуль `process` и единая команда `TransitionWorkItem` по AD-3. Покрывает FR-6.

## Boundaries & Constraints

**Always:** Смена State идёт только через `TransitionWorkItem`.

**Never:** Не писать напрямую в `state_id`.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Разрешённый переход | Открыто → В работе | State изменён | N/A |
| Запрещённый переход | Открыто → Готово | State не изменён | 422 с разрешёнными переходами |
| Удаление занятого State | В State есть Work Item | Удаление отклонено | Требуется перенос |

</frozen-after-approval>

## Code Map

- `apps/api/src/modules/process/` -- Process, Workflow, State
- `apps/api/src/modules/work/application/transition-work-item.ts` -- единая точка смены State

## Tasks & Acceptance

**Execution:**
- [x] `apps/api/src/modules/process/` -- настройка Workflow -- FR-6
- [x] `apps/api/src/modules/work/application/transition-work-item.ts` -- команда перехода -- AD-3
- [x] `apps/api/test/workflow.spec.ts` -- строки матрицы -- граничные случаи

**Acceptance Criteria:**
- Given новый Project, when он создан, then у него есть рабочий Workflow по умолчанию.

## Implementation Notes

- Смоделировано: добавлен стандартный Process, чтобы новый Project сразу был рабочим.

## Spec Change Log

## Review Triage Log

## Verification

**Commands:**
- `pnpm test --filter process` -- expected: все тесты зелёные
