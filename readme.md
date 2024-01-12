#### Задание №1

- Создайте модель для запоминания бросков 
монеты: орёл или решка.
- Также запоминайте время броска

#### Задание №2

- Доработаем задачу 1.
- Добавьте статический метод для статистики по n 
последним броскам монеты.
- Метод должен возвращать словарь с парой ключей-
значений, для орла и для решки.

#### Задание №3

- Создайте модель Автор. Модель должна содержать
следующие поля:
- имя до 100 символов
- фамилия до 100 символов
- почта
- биография
- день рождения
- Дополнительно создай пользовательское поле “полное
имя”, которое возвращает имя и фамилию.

#### Задание №4

- Создайте модель Статья (публикация). Авторы из прошлой задачи могут
писать статьи. У статьи может быть только один автор. У статьи должны быть
следующие обязательные поля:
- заголовок статьи с максимальной длиной 200 символов
- содержание статьи
- дата публикации статьи
- автор статьи с удалением связанных объектов при удалении автора
- категория статьи с максимальной длиной 100 символов
- количество просмотров статьи со значением по умолчанию 0
- флаг, указывающий, опубликована ли статья со значением по умолчанию
False

#### Задание №5

- Доработаем задачу 4.
- Создай четыре функции для реализации CRUD в модели
Django Article (статья).
- Используйте Django команды для вызова функций.

#### Задание №6

- Создайте модель Комментарий.
- Авторы могут добавлять комментарии к своим и чужим
статьям. Т.е. у комментария может быть один автор.
- И комментарий относится к одной статье. У модели должны
быть следующие поля
- автор
- статья
- комментарий
- дата создания
- дата изменения

#### Задание №7

- Создайте функции для работы с базой данных:
- Поиск всех статей автора по его имени
- Поиск всех комментариев автора по его имени
- Поиск всех комментариев по названию статьи
- Каждая из трёх функций должна иметь возможность
сортировки и ограничение выборки по количеству.
