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

##get start
```
git clone
``` 
```
cd 
```
```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
```
```
cp example.env .env
```
```
docker-compose build
```
```
docker-compose up
```
```
docker exec -it uk_djo bash
```
````
python3 manage.py migrate
```
```
cat dumps/news_3_dump_15-08-2021_21_41_00.sql | docker exec -i uk_pdb psql -U post
```