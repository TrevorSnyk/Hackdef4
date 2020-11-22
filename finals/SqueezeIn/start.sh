export PORT=3142

docker build -t squeezein .
docker run --rm -itd -e PORT=$PORT -p 3142:$PORT squeezein
