FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./mysite/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
