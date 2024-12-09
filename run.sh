# Remove existing api container if it exists
if [ "$(docker ps -aq -f name=taskmgr-api)" ]; then
    docker rm -f taskmgr-api
fi

# Remove existing db container if it exists
if [ "$(docker ps -aq -f name=taskmgr-db)" ]; then
    docker rm -f taskmgr-db
fi

# Remove existing image if it exists
if [ "$(docker images -q taskmgr:latest)" ]; then
    docker rmi taskmgr:latest
fi


# Build the new image
docker build -f Dockerfile . -t taskmgr:latest

# Run the new container
# docker run --rm --name taskmgr-api -p 8080:8080 taskmgr:latest
docker-compose up --build
