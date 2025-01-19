FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/backend

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver" ]