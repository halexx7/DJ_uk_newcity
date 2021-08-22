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


## Get start
```
git clone https://github.com/halexx7/DJ_uk_newcity.git
``` 
```
cd DJ_uk_newcity/
```
```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
```
```
cp example.env .env
```
```
docker-compose up -d
```
```
cp fake_db/full_dumps_16-08-2021_21_41_53.sql dumps/
```
```
docker-compose down
```
```
pipenv install
```
```
pipenv shell
```
```
docker-compose up -d
```
```
cat dumps/new_db_dump_17-08-2021_23_19_55.sql | docker exec -i uk_pdb psql -U post
```

Запускаем сервер
```
python3 manage.py runserver
```

Если напишет, что нужно провести миграции, проводим миграции
````
python3 manage.py migrate
```
