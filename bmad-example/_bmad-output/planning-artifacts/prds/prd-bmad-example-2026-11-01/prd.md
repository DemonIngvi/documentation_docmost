---
title: Вектор
status: final
created: 2026-11-01
updated: 2026-11-01
---

# PRD: Вектор

> Учебный пример: «Вектор» вымышленный продукт, вдохновлённый моделью работы Targetprocess. PRD создан в режиме Fast path: выводы без подтверждения человека отмечены `[ASSUMPTION]`. Числовые цели условны.

## 0. Document Purpose

Документ для руководителя продукта, UX, архитектора и разработчиков. Термины закреплены в Глоссарии. Функции сгруппированы, требования FR вложены в них и пронумерованы сквозным образом. Документ опирается на бриф, PRFAQ и исследование модели Targetprocess и не повторяет их.

## 1. Vision

Вектор это трекер работы для продуктовых организаций, устанавливаемый в контуре компании. Он даёт единую модель работы от Portfolio Epic до Task и настраиваемый Process.

Рутину вокруг трекера выполняет ИИ: разбирает Request, ищет дубли, готовит декомпозицию и строит фильтры. Главный принцип: **ИИ предлагает, человек применяет**. Никакие данные не меняются без подтверждения.

## 2. Target User

### 2.1 Jobs To Be Done

- Когда приходит крупная Feature, я хочу быстро получить качественные User Story, чтобы команда могла начать работу.
- Когда приходит Request, я хочу сразу видеть похожие, чтобы не плодить дубли.
- Когда меня спрашивают о ходе работ, я хочу собрать нужный срез за минуту, не зная языка фильтров.
- Когда команда работает над несколькими Project, я хочу планировать её загрузку одним планом.

### 2.2 Non-Users (v1)

- Команды до 10 человек: для них модель избыточна.
- Организации, которым нужен учёт затрат и тест-менеджмент в одном инструменте.

### 2.3 Key User Journeys

- **UJ-1. Лина разбивает Feature на User Story.**
  - **Persona + context:** Лина, руководитель продукта, готовит следующую итерацию.
  - **Entry state:** авторизована, открыла Feature со статусом «Анализ».
  - **Path:** нажимает «Предложить декомпозицию»; видит черновики; удаляет лишний; правит второй; нажимает «Применить».
  - **Climax:** User Story появились в Feature, в журнале видно, что предложено и что принято.
  - **Resolution:** Feature готова к планированию.
  - **Edge case:** модель недоступна; кнопка показывает причину, ручное создание работает.

- **UJ-2. Павел разбирает входящие Request.**
  - **Persona + context:** Павел, тимлид поддержки, разбирает утреннюю очередь.
  - **Entry state:** List входящих Request.
  - **Path:** открывает Request; видит блок «Похожие»; связывает с существующим или превращает в User Story.
  - **Climax:** дубль закрыт за несколько секунд.
  - **Resolution:** очередь пуста, связи сохранены.

- **UJ-3. Ирина собирает срез обычным языком.**
  - **Persona + context:** Ирина, руководитель направления, готовится к встрече.
  - **Entry state:** открыт List.
  - **Path:** пишет «баги релиза 2.3 без исполнителя»; видит построенный фильтр; проверяет; сохраняет View.
  - **Climax:** фильтр виден как обычные условия, его можно править руками.
  - **Resolution:** View сохранён и добавлен на Dashboard.

- **UJ-4. Дима ведёт работу на Board.**
  - **Persona + context:** Дима, разработчик, начинает день.
  - **Entry state:** Board своей Team Iteration.
  - **Path:** выбирает карточку; перетаскивает в следующую колонку.
  - **Climax:** карточка сменила State, запрещённый переход не сработал и объяснён.
  - **Resolution:** команда видит актуальный ход работ.

## 3. Glossary

- **Project** — контейнер работы. Каждый Work Item принадлежит ровно одному Project.
- **Program** — группа Project.
- **Team** — группа пользователей. Пользователь может входить в несколько Team.
- **Role** — набор прав пользователя в Project: Administrator, Product Owner, Developer, Observer.
- **Work Item** — общее название для Portfolio Epic, Epic, Feature, User Story, Task, Bug и Request.
- **Portfolio Epic** — верхний уровень иерархии, содержит Epic и Feature.
- **Epic** — крупная цель, содержит Feature.
- **Feature** — функция продукта, содержит User Story и Bug.
- **User Story** — работа уровня Team, помещается в одну итерацию, содержит Task и Bug.
- **Task** — часть User Story, не существует без неё.
- **Bug** — дефект, связан с User Story или Feature либо существует отдельно.
- **Request** — запрос от пользователя или заказчика, может быть превращён в User Story или Bug.
- **Process** — набор правил Project: Workflow и Custom Field. Project использует ровно один Process.
- **Workflow** — состояния и разрешённые переходы для типа Work Item.
- **State** — состояние Work Item внутри Workflow.
- **Custom Field** — дополнительное поле, заданное в Process.
- **Release** — этап Project или нескольких Project с датами.
- **Iteration** — период работы внутри Release одного Project.
- **Team Iteration** — период работы одной Team, может содержать работу из разных Project.
- **Effort** — оценка объёма в Points.
- **Velocity** — сумма Effort завершённых Work Item за Iteration или Team Iteration.
- **View** — сохранённое представление: Board, List или Roadmap.
- **Visual Encoding** — правила подсветки карточек по условиям.
- **Dashboard** — страница из нескольких View и виджетов.
- **Model Connection** — настройка подключения к языковой модели, внешней или локальной.
- **AI Suggestion** — предложение ИИ, ожидающее решения человека. Не меняет Work Item, пока не применено.
- **AI Journal** — неизменяемая запись каждого AI Suggestion и решения по нему.

## 4. Features

### 4.1 Структура и доступ

**Description:** Администратор создаёт Program, Project и Team и назначает Role. Основа для всех остальных функций. Realizes UJ-4.

**Functional Requirements:**

#### FR-1: Управление Project и Program

Administrator может создавать, архивировать и группировать Project в Program. Realizes UJ-4.

**Consequences (testable):**
- При создании Project требуется выбрать Process.
- Архивный Project скрыт из View, но его Work Item доступны по прямой ссылке.

#### FR-2: Team и Role

Administrator может создавать Team и назначать пользователю Role в Project. Realizes UJ-4.

**Consequences (testable):**
- Пользователь без Role в Project не видит его Work Item, API возвращает 404.
- Observer не может изменить Work Item, API возвращает 403.

### 4.2 Иерархия работы

**Description:** Пользователь ведёт работу в единой иерархии. Realizes UJ-1, UJ-2, UJ-4.

**Functional Requirements:**

#### FR-3: Иерархия Work Item

Product Owner может создавать Portfolio Epic, Epic, Feature, User Story и Task и связывать их по правилам иерархии. Realizes UJ-1.

**Consequences (testable):**
- Portfolio Epic, Epic, Feature и User Story могут существовать без родителя.
- Task нельзя создать без User Story.
- User Story нельзя напрямую привязать к Portfolio Epic.
- Прогресс родителя считается по доле завершённого Effort дочерних элементов.

#### FR-4: Bug

Developer может создать Bug и связать его с User Story или Feature либо оставить отдельным. Realizes UJ-4.

**Consequences (testable):**
- Bug учитывается в Velocity так же, как User Story.
- Bug может иметь не более одного родителя.

#### FR-5: Request

Любой пользователь с доступом к Project может создать Request, связать его с другим Request или превратить в User Story или Bug. Realizes UJ-2.

**Consequences (testable):**
- При превращении создаётся новый Work Item со ссылкой на исходный Request.
- Request со связью «дубль» получает State «Закрыт».

### 4.3 Process

**Description:** Project работает по настраиваемому Process. Realizes UJ-4.

**Functional Requirements:**

#### FR-6: Process и Workflow

Administrator может настроить Workflow для каждого типа Work Item: состояния и разрешённые переходы. Realizes UJ-4.

**Consequences (testable):**
- Переход вне Workflow отклоняется, API возвращает 422 с причиной.
- Удалить State, в котором есть Work Item, нельзя без переноса.

#### FR-7: Custom Field

Administrator может добавить в Process Custom Field типов «текст», «число», «список», «URL». Realizes UJ-3.

**Consequences (testable):**
- Custom Field доступен в фильтрах View.

### 4.4 Планирование

**Description:** Работа планируется по Release, Iteration и Team Iteration. Realizes UJ-4.

**Functional Requirements:**

#### FR-8: Release и Iteration

Product Owner может создавать Release и Iteration и назначать в них Work Item. Realizes UJ-4.

**Consequences (testable):**
- Iteration содержит работу только своего Project.
- User Story входит не более чем в одну Iteration.

#### FR-9: Team Iteration

Product Owner может создать Team Iteration и назначить в неё работу из разных Project. Realizes UJ-4.

**Consequences (testable):**
- User Story может одновременно входить в Iteration и Team Iteration.
- Team Iteration принадлежит ровно одной Team.

#### FR-10: Effort и Velocity

Пользователь может указать Effort, система считает Velocity. Realizes UJ-4.

**Consequences (testable):**
- Velocity пересчитывается при переходе Work Item в конечный State.
- При превышении заданной ёмкости итерации показывается предупреждение, назначение не запрещается.

### 4.5 Представления

**Description:** Один механизм View даёт разные способы увидеть работу. Realizes UJ-3, UJ-4.

**Functional Requirements:**

#### FR-11: Board

Пользователь может открыть Board, где колонки это State, и перетаскивать карточки. Realizes UJ-4.

**Consequences (testable):**
- Перетаскивание выполняет переход по FR-6.
- При превышении WIP-лимита колонка подсвечивается, перенос не запрещается.
- Изменение другого пользователя появляется на Board без перезагрузки.

#### FR-12: List и фильтры

Пользователь может открыть List, задать фильтр и сохранить его как View. Realizes UJ-3.

**Consequences (testable):**
- Фильтр поддерживает поля Work Item и Custom Field.
- View может быть личным или общим для Project.

#### FR-13: Visual Encoding

Пользователь может задать правила подсветки карточек. Realizes UJ-4.

**Consequences (testable):**
- Для карточки действует первое подходящее правило.
- Цвет сопровождается значком или текстом.

#### FR-14: Roadmap

Пользователь может открыть Roadmap, где карточки размещены на шкале времени. Realizes UJ-3.

**Consequences (testable):**
- Перемещение карточки меняет её даты.
- Диаграмма Ганта с зависимостями не поддерживается.

#### FR-15: Dashboard

Пользователь может собрать Dashboard из View и виджетов Velocity и Burndown. Realizes UJ-3.

**Consequences (testable):**
- Виджет показывает только данные, доступные пользователю по Role.

### 4.6 AI-помощники

**Description:** ИИ встроен в обычные сущности, его результат это AI Suggestion, которое применяет человек. Realizes UJ-1, UJ-2, UJ-3.

**Functional Requirements:**

#### FR-16: Model Connection

Administrator может создать Model Connection к внешнему провайдеру или локальной модели и отключить ИИ для Project. Добавлено предложением об изменении курса от 2026-11-01. Realizes UJ-1.

**Consequences (testable):**
- При локальной Model Connection запросы не уходят за пределы указанного адреса.
- Ключи не возвращаются ни одним ответом API.
- При отключённом ИИ AI-элементы не показываются.

#### FR-17: AI Journal

Система записывает каждое AI Suggestion и решение по нему. Realizes UJ-1.

**Consequences (testable):**
- Запись содержит пользователя, модель, версию промпта, дату и решение.
- Запись нельзя изменить или удалить через API.

#### FR-18: AI-декомпозиция

Product Owner может запросить декомпозицию Feature и применить предложенные User Story. Realizes UJ-1.

**Consequences (testable):**
- Каждая предложенная User Story содержит название, описание и критерии приёмки.
- Пользователь может изменить, удалить или применить каждый черновик отдельно.
- До применения в Feature не появляется новых User Story.

#### FR-19: AI-поиск дублей

При открытии Request система показывает до пяти похожих Request и Work Item. Realizes UJ-2.

**Consequences (testable):**
- Показываются только элементы, доступные пользователю по Role.
- Связь создаётся только после подтверждения.

#### FR-20: AI-фильтр

Пользователь может описать срез обычным языком и получить фильтр List. Realizes UJ-3.

**Consequences (testable):**
- Результат показан как обычные условия фильтра и редактируется вручную.
- Если запрос нельзя выразить фильтром, система сообщает об этом и не показывает приблизительный результат.

### 4.7 Открытость

**Description:** Вектор интегрируется с другими системами.

**Functional Requirements:**

#### FR-21: REST API

Интегратор может читать и менять Work Item через REST API с теми же правами, что и в интерфейсе. Realizes UJ-4.

**Consequences (testable):**
- Спецификация OpenAPI генерируется автоматически.
- Правила Workflow и Role действуют так же, как в интерфейсе.

#### FR-22: Webhook

Administrator может подписать внешний адрес на события Work Item. Realizes UJ-4.

**Consequences (testable):**
- Запрос подписан, получатель может проверить подпись.
- При ошибке доставки выполняется не менее трёх повторов.

## 5. Non-Goals (Explicit)

- Вектор не тест-менеджмент: Test Case и Test Plan не входят.
- Вектор не система учёта времени и затрат.
- ИИ не назначает исполнителей и не меняет данные сам.
- Отдельного чата с ИИ нет.
- Mashup и сторонних расширений интерфейса нет.

## 6. MVP Scope

### 6.1 In Scope

- FR-1 — FR-22.
- Развёртывание через Docker Compose.
- Веб-интерфейс на русском и английском.

### 6.2 Out of Scope for MVP

- Team Workflow: сложная настройка, перенесено в v2.
- Прогноз срыва Team Iteration: нужна история данных, v2.
- Готовые коннекторы импорта из других трекеров: v2.
- Мобильное приложение: v3.

## 7. Success Metrics

**Primary**
- **SM-1**: Доля применённых AI Suggestion — применённые к показанным, цель не менее 50 %. Validates FR-18, FR-19, FR-20.
- **SM-2**: Время декомпозиции Feature — медиана от открытия до применения, цель вдвое меньше ручного замера. Validates FR-18.

**Secondary**
- **SM-3**: Доля Request, закрытых как дубль в первый день — цель определить по пилоту. Validates FR-19.
- **SM-4**: Доля команд, ведущих работу только в Векторе через три месяца — цель 80 %. Validates FR-11, FR-12.

**Counter-metrics (do not optimize)**
- **SM-C1**: Количество созданных User Story — рост не означает пользу. Counterbalances SM-1.
- **SM-C2**: Доля применённых без правок — слишком высокая может значить невнимательную проверку. Counterbalances SM-1.

## 8. Cross-Cutting NFRs

- **NFR-1 Производительность:** Board на 2 000 карточек открывается быстрее 1,5 с на эталонном стенде.
- **NFR-2 Отклик ИИ:** 95 % AI Suggestion готовы за 20 с. Запрос не блокирует интерфейс.
- **NFR-3 Приватность:** при локальной Model Connection данные Work Item не покидают контур.
- **NFR-4 Развёртывание:** один `docker compose up` на чистом сервере.
- **NFR-5 Доступность:** WCAG 2.1 AA, Board доступен с клавиатуры.
- **NFR-6 Устойчивость:** отказ модели не влияет на работу без ИИ.
- **NFR-7 Аудит:** изменения Work Item хранятся в истории.

## 9. Open Questions

1. Какое качество декомпозиции считать достаточным и как его измерять до пилота?
2. Нужны ли промпты, настраиваемые под Process?

## 10. Assumptions Index

- `[ASSUMPTION]` §2 — размер целевой компании от 20 до 200 человек в разработке.
- `[ASSUMPTION]` §4.2 — Bug учитывается в Velocity.
- `[ASSUMPTION]` §4.5 — WIP-лимит только предупреждает.
- `[ASSUMPTION]` §8 — эталонный стенд: 4 vCPU, 8 ГБ памяти.
