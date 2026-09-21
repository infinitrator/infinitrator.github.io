# Лабораторные работы

Сайт-портфолио лабораторных работ на MkDocs.

## Структура

- `source/` — исходники MkDocs;
- `source/docs/` — страницы в Markdown;
- `.github/workflows/` — сценарий автоматической сборки и публикации.

## Тема

Используется Material for MkDocs. Выбрал её из-за нормальной навигации, хорошей читаемости и того, что она подходит для технической документации.

## Запуск локально

    cd source
    mkdocs serve

## Сборка

    mkdocs build --strict --config-file source/mkdocs.yml --site-dir ../site

После push в ветку `main` сайт автоматически собирается и публикуется через
GitHub Actions.
