---
name: Вектор
description: Спокойный плотный интерфейс для ежедневной работы с планом.
status: final
updated: 2026-11-01
colors:
  surface: '#FFFFFF'
  surface-muted: '#F4F5F7'
  ink: '#1F2733'
  ink-muted: '#5B6675'
  line: '#DDE1E7'
  primary: '#2F5BEA'
  ai: '#6B3FD4'
  ai-surface: '#F3EFFC'
  success: '#1E7F4F'
  warning: '#A86400'
  danger: '#C2342B'
typography:
  body:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    lineHeight: 20px
  title:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
rounded:
  sm: 4px
  md: 8px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
components:
  card:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.sm}'
    padding: '{spacing.2}'
  ai-suggestion:
    backgroundColor: '{colors.ai-surface}'
    rounded: '{rounded.md}'
    padding: '{spacing.3}'
---

# Вектор — Design Spine

> Учебный пример: вымышленный продукт. Режим Fast path: решения предложены ИИ.

## Brand & Style

Рабочий инструмент, а не витрина. Плотный, спокойный, без декора. Главное на экране работа, а не интерфейс.

## Colors

{colors.primary} только для основного действия. {colors.ai} только для всего, что создано ИИ: пользователь всегда отличает предложение от данных. {colors.danger} только для ошибок и опасных действий.

## Typography

Один шрифт, две роли: {typography.body} и {typography.title}.

## Layout & Spacing

Шаг 4 px. Левая панель навигации, рабочая область, карточка Work Item открывается справа и не закрывает Board.

## Elevation & Depth

Тени только у перетаскиваемой карточки и всплывающих окон.

## Shapes

Карточки {rounded.sm}, панели {rounded.md}.

## Components

- **card:** название, тип, исполнитель, Effort. Левая полоса показывает правило Visual Encoding.
- **ai-suggestion:** фон {colors.ai-surface}, пометка «Предложение ИИ», действия «Применить», «Изменить», «Отклонить».

## Do's and Don'ts

- Делай содержимое ИИ заметным цветом и подписью.
- Не передавай смысл только цветом.
- Не используй {colors.ai} для обычных кнопок.
