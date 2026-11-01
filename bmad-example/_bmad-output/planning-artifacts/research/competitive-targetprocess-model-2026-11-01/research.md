---
title: 'competitive research: модель работы Targetprocess'
type: 'competitive'
topic: 'как устроен Targetprocess и что из этого брать в Вектор'
decision: 'какие сущности и механики войдут в модель данных Вектора v1'
source: 'run'
status: final
preset: 'quick'
validation: 'citations'
created: '2026-11-01'
updated: '2026-11-01'
---

# competitive research: модель работы Targetprocess

> Учебный пример: «Вектор» вымышленный продукт и не связан с Targetprocess или IBM. Факты о Targetprocess взяты из его публичной документации, выводы для Вектора сделаны в рамках примера.

**Decision this research serves:** какие сущности и механики войдут в модель данных Вектора v1.

## Краткий вывод

Брать трёхчастную модель Targetprocess: **кто / что / когда**. Брать также иерархию работы и разделение Iteration и Team Iteration, настраиваемый Process и единый механизм View. Не брать в v1 тестирование, учёт времени, затраты и Mashup. Отдельное место Вектора: AI-слой поверх той же модели. В прочитанных страницах документации описания встроенного AI-ассистента не нашлось, но это не доказывает, что его нет.

## Находки

### Модель данных

Модель делится на три группы: People, Work и Plans [1]. Иерархия работы: Portfolio Epic, Epic, Feature, затем User Story и Bug на уровне команды [1]. Task не существует вне User Story [2]. Bug может быть связан с User Story, Feature, Release и Sprint [2]. Portfolio Epic, Epic, Feature, Bug и User Story могут существовать без родителя [1]. Portfolio Epic нельзя напрямую связать с User Story и Bug: они идут через Feature [3].

### Контейнеры и планирование

Каждый рабочий элемент принадлежит одному Project [2]. Program объединяет Project [2]. Iteration содержит работу только одного Project, а Team Iteration привязана к команде и может содержать работу из разных Project и Release [2]. Это ключевое решение для команд, работающих над несколькими продуктами.

### Процесс

Process задаёт терминологию, Workflow, практики и Custom Field, каждый Project привязан к одному Process [2]. Workflow описывает состояния и переходы, а Team Workflow сопоставляет состояния команды с общим Workflow проекта [2].

### Представления

View бывает Board, List, One-by-one и Roadmap, у каждого настраиваются карточки, линии, фильтры и Visual Encoding [2]. Kanban Board показывает состояния колонками и поддерживает WIP-лимиты [2]. Диаграмм Ганта нет, их роль выполняют Roadmap View [2]. Dashboard собирает виджеты, View и отчёты на одной странице [2].

### Оценка и интеграции

Effort задаётся в идеальных часах или абстрактных Points, Velocity считается как сумма завершённого Effort за Sprint или Team Iteration [2]. Есть публичный REST API, Webhook и Mashup [2].

## Что это значит для Вектора

| Механика Targetprocess | Решение для Вектора v1 | Почему |
| --- | --- | --- |
| Иерархия Portfolio Epic → Task | Брать полностью | Основа продукта |
| Bug отдельно от User Story | Брать | Bug может жить на уровне Feature |
| Request | Брать | Вход для AI-поиска дублей |
| Iteration и Team Iteration | Брать обе | Команды работают над несколькими Project |
| Process и Workflow | Брать | Без этого нет гибкости |
| Team Workflow | Отложить до v2 | Сложная настройка, мало нужна пилотным командам |
| Board, List, Roadmap | Брать | Основные способы работы |
| One-by-one | Не брать | Покрывается карточкой и List |
| Visual Encoding | Брать | Сильная сторона образца |
| Test Case и Test Plan | Не брать | Отдельный большой продукт |
| Учёт времени и затраты | Не брать | Не связаны с главной ценностью |
| Mashup | Не брать | Дорого поддерживать, API и Webhook достаточно |

## Противоречия и пробелы

- Документация называет контейнер то Project, то Portfolio [1][2]. В Векторе один термин: Project.
- Прочитаны только обзорные страницы. Подробности о состояниях и правилах автоматизации не изучались.
- Стоимость и доля рынка не изучались: для решения о модели данных они не нужны.

## Рекомендации

- Передать таблицу решений в PRD как границу v1.
- Сохранить термины образца в Глоссарии, чтобы пользователям Targetprocess было легко перейти.

## Источники

| № | Источник | Проверено |
| --- | --- | --- |
| 1 | [Data Model and Hierarchy](https://targetprocess.com/guide/main/data-model/) | 2026-11-01 |
| 2 | [Glossary](https://targetprocess.com/guide/how-to-start/glossary/) | 2026-11-01 |
| 3 | [Portfolio Epics](https://targetprocess.com/guide/entity-types/portfolio-epics/) | 2026-11-01 |
