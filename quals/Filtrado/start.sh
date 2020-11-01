export PORT=3120

docker build -t filtrado .
docker run --rm -it -d -e PORT=$PORT -p 3120:$PORT filtrado
