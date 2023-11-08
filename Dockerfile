LABEL org.opencontainers.image.source https://github.com/calminaro/calminaro_sito_flask

FROM python

WORKDIR /flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py ./app.py
COPY ./credenziali.json ./credenziali.json
COPY ./templates ./templates
COPY ./static ./static

CMD ["gunicorn",  "-w 3", "-b 0.0.0.0",  "app:app"]
