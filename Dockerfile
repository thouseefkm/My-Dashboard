FROM python:3.4

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./ ./

RUN pip install -r requirements.txt

RUN python manage.py makemigrations \
    && python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

