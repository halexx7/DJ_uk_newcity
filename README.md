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

cat dumps/news_3_dump_15-08-2021_21_41_00.sql | docker exec -i uk_pdb psql -U post

pg_dumpall -c -U post > code/dumps/news_2_dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql