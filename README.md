# Artrey_shop_task

### Цель данного API сервиса:
- Получать запрошенные колонки
- Фильтровать данные по одной или нескольким колонкам: дате (from/to), магазинам, странам
- Группировать данные по одной или нескольким колонкам: датам, магазинам, странам
- Сортировать по любой из колонок
- Если не указано, какие колонки необходимо отобразить, то отобразятся все колонки.

### Технологии
Python, Django, DRF, django-filter, pandas

### Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке:
- Установите и активируйте виртуальное окружение:
```
Для пользователей Windows:
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Перейдите в каталог с файлом manage.py выполните команды:
Выполнить миграции:
```
python manage.py migrate
```
Перейдите в каталог с файлом csv_to_bd.py и запустите его, чтобы наполнить бд данными:
```
python csv_to_bd.py
```
Запуск проекта:
```
python manage.py runserver
```
# В данном проекте использовано LimitOffsetPagination, по умолчанию на 100 записей. Для изминения перейдите в settings.py

### Ссылка на использованные данные:
```
Dataset: https://gist.github.com/artrey/8d6a3f2d91cefb5e6343bedbc9ef8c79
```
### Примеры
---
Примеры запросов (ваши запросы могут отличаться, главное, чтобы они выполняли поставленную задачу):

1. Показать сырые данные вида `Date - Visitors - Earnings`
```bash
api/v1/metrics/?show=date&show=visitors&show=earnings
```
2. Показать сырые данные вида `Date - Country - Visitors - Earnings` за промежуток с 2021-03-20 по 2021-06-01
```bash
api/v1/metrics/?show=date&show=country&show=visitors&show=earnings&date_from=2021-03-20&date_to=2021-06-01
```
3. Показать сгруппированные данные по странам, при этом отобразить `Earnings` и упорядочить по убыванию по `Earnings`
```bash
api/v1/metrics/?group=country&show=earnings&o=-earnings
```
4. Показать сгруппированные данные по магазинам и странам и при этом отобразить `Visitors`
```bash
api/v1/metrics/?group=country&group=shop&show=visitors
```
