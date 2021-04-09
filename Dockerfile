FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt && pip install Pillow
RUN pip install isort && pip install black
RUN apt-get update && apt-get -y install vim nano
COPY . /code/