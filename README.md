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
pipenv install
```
```
pipenv shell
```
```
cp fake_db/02_new_db_dump_23-08-2021_21_40_06.sql dumps/
```
```
docker-compose up -d
```
```
cat dumps/02_new_db_dump_23-08-2021_21_40_06.sql | docker exec -i uk_pdb psql -U post
```

Запускаем сервер
```
python3 manage.py runserver
```

## ЕСЛИ НАПИШЕТ, что нужно провести миграции, проводим миграции
````
python3 manage.py migrate
```

