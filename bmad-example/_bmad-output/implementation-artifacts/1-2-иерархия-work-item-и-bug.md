---
title: 'Иерархия Work Item и Bug'
type: 'feature'
created: '2026-11-01'
status: 'done'
route: 'dispatch'
review_loop_iteration: 1
context:
  - '{project-root}/_bmad-output/planning-artifacts/architecture/architecture-bmad-example-2026-11-01/ARCHITECTURE-SPINE.md'
---

> Учебный пример: реализация смоделирована, код не написан. Записи о тестах и ревью показывают форму документа, это не результаты реальных запусков.

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Работу нельзя разбить по уровням.

**Approach:** Единая таблица `work_item` и `HierarchyPolicy` по AD-2. Покрывает FR-3 и FR-4.

## Boundaries & Constraints

**Always:** Все правила связей находятся в `HierarchyPolicy`. Прогресс родителя считается по завершённому Effort.

**Never:** Не создавать таблицу под каждый тип Work Item.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Полная цепочка | Portfolio Epic → Task | Связи сохранены | N/A |
| Task без родителя | Нет User Story | Не создан | 422 |
| User Story под Portfolio Epic | Прямая связь | Отклонена | 422 с разрешёнными родителями |
| Цикл | Родитель становится потомком | Отклонён | 422 |
| Bug с двумя родителями | User Story и Feature | Отклонён | 422 |

</frozen-after-approval>

## Code Map

- `apps/api/src/modules/work/domain/hierarchy-policy.ts` -- правила связей
- `apps/api/src/modules/work/adapters/` -- REST и БД

## Tasks & Acceptance

**Execution:**
- [x] `apps/api/src/modules/work/domain/hierarchy-policy.ts` -- правила -- AD-2
- [x] `apps/api/src/modules/work/application/` -- команды создания и связи -- FR-3, FR-4
- [x] `apps/api/test/hierarchy.spec.ts` -- строки матрицы -- граничные случаи

**Acceptance Criteria:**
- Given Feature с дочерними User Story, when часть завершена, then прогресс равен доле завершённого Effort.

## Implementation Notes

- Смоделировано: проверка циклов выполнена рекурсивным запросом.

## Spec Change Log

- Смоделировано. Находка ревью: матрица не описывала циклы. Добавлена строка «Цикл». Известно плохое состояние: зависание подсчёта прогресса.

## Review Triage Log

| Находка | Вердикт | Обоснование |
|---------|---------|-------------|
| Цикл в иерархии вешает подсчёт | high | Смоделировано: исправлено, добавлена строка матрицы |

## Verification

**Commands:**
- `pnpm test --filter work` -- expected: все тесты зелёные
