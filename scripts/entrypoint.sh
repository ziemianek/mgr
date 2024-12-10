#!/bin/bash
set -e

# Variables
# DB_HOST=${DB_HOST:-localhost}
# DB_PORT=${DB_PORT:-3306}
# DB_USER=${DB_USER:-root}
# DB_PASSWORD=${DB_PASSWORD:-root}
# DB_NAME=${DB_NAME:-task_manager}

# Wait for MySQL server to be ready
# echo "Waiting for MySQL to be ready..."
# until mysqladmin ping -h "$DB_HOST" -P "$DB_PORT" --silent; do
#     echo -n "."
#     sleep 1
# done
# echo "MySQL is ready."

mysqladmin ping -h localhost -P 3306 

# # Check if schema.sql exists
# if [ -f "/docker-entrypoint-initdb.d/schema.sql" ]; then
#     echo "schema.sql found. Loading into database..."
#     mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" --password="$DB_PASSWORD" "$DB_NAME" < /docker-entrypoint-initdb.d/schema.sql
# else
#     echo "schema.sql not found"
#     exit 1
# fi

# # Run default CMD from the base image
# exec "$@"
