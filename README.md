# Тестовое задание
## Приложение для создания и отрисовки меню
### Задание: создать django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию

### Описание приложения:
* Меню реализовано через template tag
* Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
* Хранится в БД.
* Редактируется в стандартной админке Django
* Активный пункт меню определяется исходя из URL текущей страницы
* Меню на одной странице может быть несколько. Они определяются по названию.
* При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
* На отрисовку каждого меню требуется ровно 1 запрос к БД

### Решение:
* Для древовидного меню использовал django-mptt
* Создал два класса(Menu и MenuItem)
* Написал простые views для рендера html страницы
* Прописал роутинг
* Создал базовые html странички и новый тег для возможности нарисовать меню по названию({% draw_menu 'main_menu' %})


### Запуск проекта и работа с ним
См. [документацию](DOCUMENTATION.md)
