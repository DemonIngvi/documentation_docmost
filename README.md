# documentation_docmost

Рабочая папка: BMAD Method, Docmost и полный пример документации на вымышленном AI-трекере «Вектор».

| Папка | Что внутри |
| --- | --- |
| `bmad-example/` | Проект с BMAD 6.12.4 и всеми документами примера (`_bmad-output/`) |
| `docmost/` | Docmost 0.97.0 в Docker внутри WSL |
| `tools/` | Скрипты проверки и публикации |

## Docmost

Запуск: `D:\documentation\docmost\start-docmost.ps1`. Откроется <http://localhost:3100>, данные для входа лежат в `docmost/admin-credentials.txt`.

Остановка: `D:\documentation\docmost\stop-docmost.ps1`. Данные сохраняются.

После перезагрузки компьютера Docmost нужно запустить скриптом: WSL не стартует сам, а без удерживающего процесса гасит виртуальную машину при простое.

База и файлы хранятся в томах Docker внутри Ubuntu в WSL, а не на диске D. Файлы `docmost/.env` и `docmost/admin-credentials.txt` содержат секреты, их нельзя публиковать.

## BMAD

Папки `bmad-example/_bmad` и `bmad-example/.claude` в репозиторий не входят, их создаёт установка. После клонирования выполните команду ниже в `bmad-example`. Для запуска Docmost скопируйте `docmost/.env.example` в `docmost/.env` и задайте свои секреты.

Откройте `D:\documentation\bmad-example` в Claude Code и вызовите `/bmad-help`: навык подскажет следующий шаг. Для нового проекта установите BMAD в его папку:

```
npx bmad-method@6.12.4 install --directory . --modules bmm --tools claude-code --communication-language Russian --document-output-language Russian --yes
```

## Обновление примера в Docmost

После правки документов:

```
python D:\documentation\tools\check_traceability.py
python D:\documentation\tools\publish_to_docmost.py
```

Публикация заменяет все страницы пространства «Вектор: пример BMAD», поэтому правки, сделанные прямо в Docmost, будут потеряны. Источник правды это файлы на диске.
