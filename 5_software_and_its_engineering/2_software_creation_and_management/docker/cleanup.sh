docker system prune

echo "deleting all containers"
docker rm -vf $(docker ps -aq)
echo "done"

echo "deleting all images"
docker image rm $(docker images -aq)
echo "done"
