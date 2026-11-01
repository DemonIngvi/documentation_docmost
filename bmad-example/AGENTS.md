<!-- bmad:context -->
<!-- Учебный пример. Создан 2026-11-01 без проверки по коммиту: кода Вектора нет, команды показывают форму блока. Managed by bmad-project-context. -->

## Вектор

Трекер работы с AI-помощниками, вымышленный учебный продукт. TypeScript, NestJS, React, PostgreSQL, Redis. Планирование лежит в `_bmad-output/planning-artifacts/`, статус спринта в `_bmad-output/implementation-artifacts/sprint-status.yaml`.

## Policy

- Никогда не применяй AI Suggestion автоматически; применение всегда идёт от запроса пользователя.
- Никогда не пиши в `state_id` напрямую; используй `TransitionWorkItem`.

## Where things are

- Решения архитектуры: `_bmad-output/planning-artifacts/architecture/`, правила AD обязательны.
- Термины: Глоссарий в PRD; используй их без синонимов.

## Running and verifying

- Запускай `docker compose up -d` перед интеграционными тестами.
- Запускай `pnpm test --filter <модуль>` во время работы, полный набор только перед ревью.

## Conventions that differ from defaults

- Передавай `ProjectScope` в каждый запрос чтения, иначе код не компилируется.
- Отдавай ошибки API в формате RFC 9457.

## Known pitfalls

- Не пиши текст Work Item и промпты в логи: это нарушает NFR-3.

<!-- /bmad:context -->
