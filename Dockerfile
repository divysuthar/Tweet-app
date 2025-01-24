FROM python:3

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /backend

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver" ]