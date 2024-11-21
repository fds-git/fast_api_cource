# fast_api_cource
FastApi Cource

Миграции
Инициализация: в devcontainer (выполняется при первичной настройке репозитория)
alembic init migrations
после чего alembic.ini переложить в корень проекта и выполнить настройки app/migrations/env.py в соответствии с уроком

Сделать миграцию:
зайти в запущенной системе в контейнер
активировать виртуальное окружение
python -m poetry shell
Создать миграцию
docker exec -it api bash
alembic revision --autogenerate -m "Initial migration"
или
docker exec -it api alembic revision --autogenerate -m "Initial migration"
или
docker compose exec main alembic revision --autogenerate -m "Initial migration"

Прогнать все миграции
docker exec -it api alembic upgrade head

Откатиться на 1 шаг назад
docker exec -it api alembic downgrade -1

Посмотреть что в базе 
docker exec -it postgres bash
psql -u postgres -p postgres
Посмотреть все таблицы - \dt
Либо через pgadmin (вкладка браузера должна быть открыта после подъема контейнера)
127.0.0.1:5050