# documentation_docmost

Полный пример документации на вымышленном AI-трекере «Вектор». Он устроен по образцу модели Targetprocess, но с ним не связан. Документы созданы по методу BMad Method.

Что здесь настоящее, а что смоделировано, написано на странице `bmad-example/docs/index.md`.

| Папка | Что внутри |
| --- | --- |
| `bmad-example/_bmad-output/` | Документы проекта |
| `bmad-example/docs/architecture/` | Архитектура в YAML, источник для Spine |
| `bmad-example/_quality/` | Результаты проверок и журнал расхода токенов |

Как устроены репозитории и как создать такой проект, описано в [doc-rules](https://github.com/DemonIngvi/doc-rules/blob/main/docs/new-project.md).

## Публикация в Docmost

```
uv run ../doc-publisher/tools/publish.py --root bmad-example
```

Публикация заменяет страницы пространства, поэтому источник правды это файлы, а не Docmost.
