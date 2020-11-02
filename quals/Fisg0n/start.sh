export PORT=3142

docker build -t fisg0n .
docker run --rm -itd -e PORT=$PORT -p 3142:$PORT fisg0n && echo "[ ok ] Application is running on port " $PORT
docker exec -it $(docker ps -aqf "ancestor=fisg0n") /etc/init.d/cron start

export CONTAINER_IP=$(docker exec -it $(docker ps -aqf "ancestor=fisg0n") hostname -i|tr -d '\r')

if [ "$CONTAINER_IP" != "172.17.0.2" ];
then
    echo "[ ! ] Antes de comenzar, por favor reemplace IP en la línea #14 del archivo /app/app/admin/admin_typing_pwd.py por: ${CONTAINER_IP}"
fi


