---
status: final
stepsCompleted: [validate-prerequisites, design-epics, create-stories, final-validation]
inputDocuments:
  - _bmad-output/planning-artifacts/prds/prd-bmad-example-2026-11-01/prd.md
  - _bmad-output/planning-artifacts/architecture/architecture-bmad-example-2026-11-01/ARCHITECTURE-SPINE.md
  - _bmad-output/planning-artifacts/ux-designs/ux-bmad-example-2026-11-01/EXPERIENCE.md
---

# Вектор - Epic Breakdown

> Учебный пример: вымышленный продукт.

## Overview

Документ разбивает требования PRD, UX и архитектуры на эпики и истории, которые можно реализовывать.

## Requirements Inventory

### Functional Requirements

FR-1 — FR-23, формулировки в PRD §4.

### NonFunctional Requirements

NFR-1 — NFR-7, формулировки в PRD §8.

### Additional Requirements

- Архитектура: модульный монолит, правила AD-1 — AD-12 обязательны для всех историй.
- Первая история создаёт каркас проекта и `docker-compose.yml`.

### UX Design Requirements

- Содержимое ИИ всегда отмечено цветом и подписью.
- Перенос карточек доступен с клавиатуры.
- Подсветка дублируется значком или текстом.

### FR Coverage Map

| FR | История |
| --- | --- |
| FR-1 | 1.1 |
| FR-2 | 1.1 |
| FR-3 | 1.2 |
| FR-4 | 1.2 |
| FR-5 | 4.1 |
| FR-6 | 1.3 |
| FR-7 | 4.2 |
| FR-8 | 3.1 |
| FR-9 | 3.2 |
| FR-10 | 3.3 |
| FR-11 | 2.1 |
| FR-12 | 2.2 |
| FR-13 | 2.3 |
| FR-14 | 2.4 |
| FR-15 | 2.5 |
| FR-16 | 5.1 |
| FR-17 | 5.2 |
| FR-18 | 5.3 |
| FR-19 | 5.4 |
| FR-20 | 5.5 |
| FR-21 | 4.3 |
| FR-22 | 4.4 |
| FR-23 | 1.1 |

## Epic List

1. Рабочая модель: команда ведёт работу в единой иерархии по своему Process.
2. Представления: команда видит работу на Board, List, Roadmap и Dashboard.
3. Планирование: команда планирует работу по итерациям.
4. Вход и интеграции: заявки и внешние системы подключены к работе.
5. AI-помощники: рутину готовит ИИ, решения принимает человек.

## Epic 1: Рабочая модель

Команда может завести Project и вести работу в единой иерархии по настроенному Process.

### Story 1.1: Project, Team и Role

As a Administrator,
I want создать Project, Team и назначить Role,
So that команда начала работать с нужными правами.

**Acceptance Criteria:**

**Given** чистая установка через `docker compose up` по NFR-4 и заданные `ADMIN_EMAIL` и `ADMIN_PASSWORD`
**When** Administrator входит и создаёт Project с Process
**Then** Project появляется в списке
**And** пользователь без Role получает 404 на Work Item этого Project

**Given** пользователь с Role Observer
**When** он пытается изменить Work Item
**Then** API возвращает 403

**Given** неверный пароль
**When** пользователь входит
**Then** API возвращает 401 без указания, что именно неверно

**Given** Project с таким именем уже есть в Program
**When** Administrator создаёт Project
**Then** API возвращает 409 с кодом `project_name_taken`

### Story 1.2: Иерархия Work Item и Bug

As a Product Owner,
I want создавать Work Item и связывать их по правилам иерархии,
So that работа разбита на понятные уровни.

**Acceptance Criteria:**

**Given** существует Project
**When** Product Owner создаёт Portfolio Epic, Epic, Feature, User Story и Task
**Then** связи сохраняются, а прогресс родителя считается по завершённому Effort

**Given** User Story без родителя
**When** пользователь пытается привязать её к Portfolio Epic
**Then** API возвращает 422 со списком разрешённых родителей

**Given** попытка создать Task без User Story
**When** запрос отправлен
**Then** Task не создаётся

**Given** Developer создаёт Bug
**When** он указывает User Story или Feature
**Then** Bug связан с указанным родителем, а при двух родителях API возвращает 422

**Given** изменён Work Item
**When** пользователь открывает его историю по NFR-7
**Then** видны автор, время, поле, старое и новое значение

### Story 1.3: Process и Workflow

As a Administrator,
I want настроить состояния и переходы,
So that работа шла по процессу команды.

**Acceptance Criteria:**

**Given** Process с Workflow для User Story
**When** выполняется запрещённый переход
**Then** API возвращает 422 с причиной

**Given** State, в котором есть Work Item
**When** Administrator удаляет его
**Then** система требует перенести Work Item

## Epic 2: Представления

Команда видит работу в удобной форме и сохраняет свои срезы.

### Story 2.1: Board

As a Developer,
I want двигать карточки по колонкам,
So that команда видела реальный ход работ.

**Acceptance Criteria:**

**Given** Board с колонками по State
**When** Developer переносит карточку
**Then** выполняется переход Workflow, другие пользователи видят его без перезагрузки

**Given** колонка с превышенным WIP-лимитом
**When** карточка попадает в неё
**Then** колонка подсвечивается, перенос не запрещается

**Given** пользователь работает только с клавиатурой
**When** он использует `Space` и стрелки
**Then** он может перенести карточку, экран соответствует WCAG 2.1 AA по NFR-5

**Given** Board на 2 000 карточек на эталонном стенде
**When** пользователь открывает его
**Then** Board открывается быстрее 1,5 с по NFR-1

### Story 2.2: List и фильтры

As a руководитель направления,
I want отфильтровать работу и сохранить View,
So that нужный срез был под рукой.

**Acceptance Criteria:**

**Given** List
**When** пользователь задаёт условия и сохраняет View
**Then** View открывается с теми же условиями и может быть личным или общим

### Story 2.3: Visual Encoding

As a тимлид,
I want задать правила подсветки,
So that риски были заметны на Board.

**Acceptance Criteria:**

**Given** несколько правил
**When** карточка подходит под два из них
**Then** действует первое, цвет дублируется значком

### Story 2.4: Roadmap

As a руководитель направления,
I want видеть работу на шкале времени,
So that я мог обсуждать сроки.

**Acceptance Criteria:**

**Given** Roadmap с Feature
**When** пользователь передвигает карточку
**Then** даты Feature меняются

### Story 2.5: Dashboard

As a руководитель направления,
I want собрать Dashboard из View и виджетов,
So that видеть состояние работ на одной странице.

**Acceptance Criteria:**

**Given** Dashboard с виджетами Velocity и Burndown
**When** его открывает пользователь с меньшими правами
**Then** виджет показывает только доступные ему данные

## Epic 3: Планирование

Команда планирует работу по Release, Iteration и Team Iteration.

### Story 3.1: Release и Iteration

As a Product Owner,
I want создавать Release и Iteration,
So that работа Project имела сроки.

**Acceptance Criteria:**

**Given** Iteration одного Project
**When** в неё назначают User Story другого Project
**Then** назначение отклоняется

### Story 3.2: Team Iteration

As a Product Owner,
I want планировать работу Team из разных Project,
So that у команды был один план.

**Acceptance Criteria:**

**Given** Team Iteration
**When** в неё назначают User Story из двух Project
**Then** обе отображаются в одном плане

### Story 3.3: Effort и Velocity

As a тимлид,
I want видеть Velocity и загрузку,
So that план был реалистичным.

**Acceptance Criteria:**

**Given** Work Item с Effort переходит в конечный State
**When** переход завершён
**Then** Velocity итерации пересчитана

**Given** ёмкость итерации превышена
**When** назначается новая работа
**Then** показывается предупреждение, назначение не запрещается

## Epic 4: Вход и интеграции

Заявки и внешние системы подключены к работе команды.

### Story 4.1: Request

As a тимлид поддержки,
I want принимать и обрабатывать Request,
So that запросы превращались в работу.

**Acceptance Criteria:**

**Given** Request
**When** пользователь превращает его в User Story
**Then** новая User Story ссылается на Request

**Given** Request связан как дубль
**When** связь сохранена
**Then** Request получает State «Закрыт»

### Story 4.2: Custom Field

As a Administrator,
I want добавлять поля в Process,
So that учитывать особенности команды.

**Acceptance Criteria:**

**Given** Custom Field типа «список»
**When** пользователь заполняет его
**Then** значение доступно в фильтрах View

### Story 4.3: REST API

As a интегратор,
I want работать с Work Item через API,
So that подключить другие системы.

**Acceptance Criteria:**

**Given** API-токен пользователя
**When** выполняется запрещённый переход
**Then** действуют те же правила, что и в интерфейсе

**Given** сборка приложения
**When** она завершена
**Then** спецификация OpenAPI сгенерирована

### Story 4.4: Webhook

As a Administrator,
I want подписать внешний адрес на события,
So that другие системы узнавали об изменениях.

**Acceptance Criteria:**

**Given** подписка
**When** Work Item меняется
**Then** отправляется подписанный запрос

**Given** получатель недоступен
**When** доставка не удалась
**Then** выполняется не менее трёх повторов

## Epic 5: AI-помощники

Рутину готовит ИИ, решения принимает человек.

### Story 5.1: Model Connection

As a Administrator,
I want подключить внешнюю или локальную модель,
So that ИИ работал по правилам компании.

**Acceptance Criteria:**

**Given** локальная Model Connection
**When** выполняется запрос к ИИ
**Then** сетевой обмен идёт только с указанным адресом, данные Work Item не покидают контур по NFR-3

**Given** сохранённый ключ
**When** настройки читаются через API
**Then** ключ не возвращается

**Given** ИИ отключён для Project
**When** пользователь открывает Feature
**Then** AI-элементы не показываются

### Story 5.2: AI Journal

As a Administrator,
I want видеть журнал работы ИИ,
So that можно было проверить любое решение.

**Acceptance Criteria:**

**Given** создано AI Suggestion
**When** пользователь принимает решение
**Then** в журнале есть пользователь, модель, версия промпта, дата и решение

**Given** запись журнала
**When** кто-либо пытается изменить её
**Then** изменение невозможно

### Story 5.3: AI-декомпозиция Feature

As a Product Owner,
I want получить черновики User Story,
So that быстрее готовить работу к планированию.

**Acceptance Criteria:**

**Given** Feature с описанием
**When** Product Owner запрашивает декомпозицию
**Then** черновики содержат название, описание и критерии приёмки, интерфейс при этом не блокируется

**Given** черновики показаны
**When** пользователь ещё не применил их
**Then** новых User Story в Feature нет

**Given** черновики применены
**When** прошло меньше 30 секунд
**Then** применение можно отменить

**Given** модель недоступна
**When** пользователь нажимает кнопку
**Then** показывается причина, ручное создание работает по NFR-6

**Given** эталонная модель
**When** выполнено 100 запросов декомпозиции
**Then** 95 AI Suggestion готовы за 20 с, интерфейс не блокируется по NFR-2

### Story 5.4: AI-поиск дублей

As a тимлид поддержки,
I want видеть похожие Request,
So that не создавать дубли.

**Acceptance Criteria:**

**Given** открыт Request
**When** есть похожие элементы
**Then** показано до пяти элементов, доступных пользователю

**Given** показан похожий элемент
**When** пользователь подтверждает дубль
**Then** связь создаётся только после подтверждения

### Story 5.5: AI-фильтр

As a руководитель направления,
I want описать срез обычным языком,
So that не изучать язык фильтров.

**Acceptance Criteria:**

**Given** запрос обычным языком
**When** его можно выразить фильтром
**Then** результат показан как обычные условия

**Given** запрос нельзя выразить фильтром
**When** модель ответила
**Then** система сообщает об этом и не показывает приблизительный результат
