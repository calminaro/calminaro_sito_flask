# Sito web personale

Comandi per fare il Build del Docker e primo avvio:

docker build -t ghcr.io/calminaro/sito-calminaro:TAG .

docker run -p 8000:8000 ghcr.io/calminaro/sito-calminaro:TAG
