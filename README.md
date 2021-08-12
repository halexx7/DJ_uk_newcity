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

Get Start

docker-compose build
docker-compose up

cat fake_db/dump_09-08-2021_21_14_03.sql | docker exec -i uk_pdb psql -U post
docker exec -it uk_djo bash

python3 manage.py migrate