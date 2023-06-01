FROM python:3.8

WORKDIR /flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py ./app.py
COPY ./credenziali.json ./credenziali.json
COPY ./templates ./templates
COPY ./static ./static

CMD ["gunicorn",  "-w 4", "-b 0.0.0.0",  "app:app"]
