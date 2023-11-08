# Sito web personale

Comandi utili per il deploy tramite Docker

`docker pull ghcr.io/calminaro/sito-calminaro:TAG`

`docker run -p 8000:8000 ghcr.io/calminaro/sito-calminaro:TAG`

oppure

`git clone https://github.com/calminaro/calminaro_sito_flask.git`

`cd calminaro_sito_flask`

`docker build calminaro_sito_flask`

`docker run -p 8000:8000 calminaro_sito_flask`

---

Questo è il repository di un sito web personale, l'utilizzo come template base è permesso previa rimozione dei dati.
