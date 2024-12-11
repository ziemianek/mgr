#!/bin/bash

remove_container() {
    local container_name=$1
    if [ "$(docker ps -aq -f name=$container_name)" ]; then
        docker rm -f $container_name
        echo "Removed existing container: $container_name"
    else
        echo "No existing container found: $container_name"
    fi
}

remove_image() {
    local image_name=$1
    if [ "$(docker images -q $image_name)" ]; then
        docker rmi $image_name
        echo "Removed existing image: $image_name"
    else
        echo "No existing image found: $image_name"
    fi
}

build_image() {
    local dockerfile=$1
    local image_name=$2
    docker build -f $dockerfile . -t $image_name
    echo "Built new image: $image_name"
}

run_containers() {
    docker-compose -p taskmgr up --build
}

# Main script execution
remove_container "taskmgr-api-1"
remove_container "taskmgr-mysql-1"
docker volume rm mgr_mysql_data

remove_image "taskmgr/api:latest"
build_image "Dockerfile" "taskmgr/api:latest"

run_containers