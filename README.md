
# Древовидное меню для Django

Это Django приложение предоставляет функционал для создания и управления древовидным меню через админ-панель Django.

## Особенности

- Поддержка древовидной структуры меню.
- Реализация меню через пользовательский template tag.
- Управление меню через стандартную админку Django.
- Автоматическое раскрытие активного пункта меню и его родительских пунктов.
- Поддержка нескольких меню на одной странице.
- Определение активного пункта меню по URL.
- Поддержка как статических, так и именованных URL в пунктах меню.

## Установка

Для использования приложения выполните следующие шаги:

1. Клонируйте репозиторий в ваш проект:

```
git clone https://github.com/Abdunazarov/menu-tree.git
```


2. Добавьте `menu_tree_app` в `INSTALLED_APPS` в вашем файле `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'menu_tree_app',
    # ...
]
```

3. Выполните миграции для создания необходимых таблиц в базе данных:

```
python manage.py makemigrations menu_tree_app
python manage.py migrate
```

## Использование

Чтобы добавить меню на страницу, используйте пользовательский template tag `draw_menu` в шаблоне:

```html
{% load menu_tags %}
<body>
    ...
    {% draw_menu 'имя_меню' %}
    ...
</body>
```

Замените `'имя_меню'` на имя вашего меню, которое вы хотите отобразить.

## Управление меню

Для добавления и настройки пунктов меню используйте админ-панель Django. Перейдите в раздел "Menu items" и добавьте нужные пункты меню, указывая их родителей для создания иерархии.

