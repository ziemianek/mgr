.PHONY: remove_container remove_image build_image run_containers

remove_container:
    @container_name=$(name) && \
    if [ "$$(docker ps -aq -f name=$$container_name)" ]; then \
        docker rm -f $$container_name; \
        echo "Removed existing container: $$container_name"; \
    else \
        echo "No existing container found: $$container_name"; \
    fi

remove_image:
    @image_name=$(name) && \
    if [ "$$(docker images -q $$image_name)" ]; then \
        docker rmi $$image_name; \
        echo "Removed existing image: $$image_name"; \
    else \
        echo "No existing image found: $$image_name"; \
    fi

build_image:
    @dockerfile=$(dockerfile) && image_name=$(name) && \
    docker build -f $$dockerfile . -t $$image_name && \
    echo "Built new image: $$image_name"

run:
    @if [ -f docker-compose.yml ]; then \
        docker-compose -p taskmgr up --build; \
    else \
        echo "docker-compose.yml file not found"; \
        exit 1; \
    fi

clean:
    @$(MAKE) remove_container name=taskmgr-api-1
    @$(MAKE) remove_container name=taskmgr-mysql-1

rebuild: clean
    @$(MAKE) remove_image name=taskmgr/api:latest
    @$(MAKE) build_image dockerfile=Dockerfile name=taskmgr/api:latest
    @$(MAKE) run