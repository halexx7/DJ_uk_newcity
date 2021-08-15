# CRM для УК

CRM для работы управляющей компании на Django.

## Стек

* Python>3.5
* Django 2
* VSCode
* PostgreSQL
* Docker
* Docker-compose

## Лицензия

MIT

get start

docker-compose up

docker exec -it uk_djo bash

python3 manage.py migrate

cat dumps/empty_dump_15-08-2021_11_07_30.sql | docker exec -i uk_pdb psql -U post

