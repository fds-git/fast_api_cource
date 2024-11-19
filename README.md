# fast_api_cource
FastApi Cource

Миграции
Инициализация: в devcontainer
alembic init migrations

Сделать миграцию:
зайти в запущенной системе в контейнер
активировать виртуальное окружение
python -m poetry shell
Запустить миграцию
alembic revision --autogenerate -m "Initial migration"
