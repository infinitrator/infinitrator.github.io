# Лабораторная работа №3

## CI/CD для статического сайта в SourceCraft

## Цель работы

Настроить автоматическую сборку и публикацию одного MkDocs-сайта на двух
платформах: SourceCraft Sites и GitHub Pages.

## Структура репозитория

В работе используется один локальный Git-репозиторий и два удалённых:

- `origin` — репозиторий на GitHub;
- `sourcecraft` — репозиторий на SourceCraft.

Основные файлы проекта:

```text
.
├── .github/workflows/deploy-pages.yml
├── .sourcecraft/ci.yaml
├── .sourcecraft/sites.yaml
├── requirements.txt
└── source/
    ├── mkdocs.yml
    └── docs/
```

Markdown-исходники сайта находятся в `source/docs`, а настройки MkDocs — в
`source/mkdocs.yml`. Обе платформы собирают сайт из одних и тех же исходников.

## Настройка GitHub Actions

В файле `.github/workflows/deploy-pages.yml` создан workflow, который запускается
при каждом push в ветку `main`.

Workflow выполняет следующие действия:

1. Загружает содержимое репозитория.
2. Устанавливает Python 3.12.
3. Устанавливает зависимости из `requirements.txt`.
4. Выполняет строгую сборку MkDocs в каталог `site`.
5. Загружает результат как артефакт GitHub Pages.
6. Публикует артефакт с помощью `actions/deploy-pages`.

В настройках GitHub-репозитория в разделе `Settings → Pages` в качестве
источника публикации выбран `GitHub Actions`.

## Настройка SourceCraft

В SourceCraft были созданы публичная организация и публичный репозиторий. Для
работы с репозиторием по HTTPS был создан персональный токен с ролью Maintainer.

Конфигурация `.sourcecraft/ci.yaml` запускает workflow `build-site` после push в
ветку `main`. Он устанавливает зависимости, собирает MkDocs-сайт в каталог
`site`, создаёт ветку `release` и отправляет в неё результат сборки.

Файл `.sourcecraft/sites.yaml` указывает SourceCraft Sites публиковать каталог
`site` из ветки `release`:

```yaml
site:
  root: site
  ref: release
```

Репозиторий и организация должны быть публичными. Основной веткой назначена
ветка `main`, а для ветки `release` не устанавливалась политика, запрещающая
CI/CD-процессу выполнять force push.

## Порядок развертывания

После изменения исходников выполняются две команды:

```bash
git push origin main
git push sourcecraft main
```

На GitHub запускается GitHub Actions, а на SourceCraft — workflow из файла
`.sourcecraft/ci.yaml`. Локально собирать готовый HTML для публикации не нужно.

## Проверка результата

- GitHub Actions завершился со статусом `Success`.
- SourceCraft CI/CD завершился со статусом `Успех`.
- В SourceCraft появилась ветка `release` с каталогом `site`.
- Обе опубликованные версии сайта открываются по HTTPS.

## Ссылки

1. [Сайт на GitHub Pages](https://infinitrator.github.io/)
2. [Репозиторий на GitHub](https://github.com/infinitrator/infinitrator.github.io)
3. Сайт на SourceCraft: `SOURCECRAFT_SITE_URL`
4. Репозиторий на SourceCraft: `SOURCECRAFT_REPOSITORY_URL`

## Вывод

В ходе работы был настроен CI/CD для одного MkDocs-проекта на двух платформах.
Теперь после отправки изменений в ветку `main` сайт автоматически собирается и
публикуется на GitHub Pages и SourceCraft Sites. Такой подход исключает ручную
сборку опубликованной версии и позволяет воспроизводимо развернуть сайт из
исходников репозитория.
