export PORT=3120

docker build -t johnniewalker .
docker run --rm -it -d -e PORT=$PORT -p 3120:$PORT johnniewalker
