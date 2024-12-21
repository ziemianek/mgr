#!/bin/bash

# exec from root directory

# Path to the .env file
ENV_FILE=".env"

# Check if the file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "File $ENV_FILE does not exist."
    exit 1
fi

# Export each variable from the .env file
export $(grep -v '^#' "$ENV_FILE" | xargs)

echo "Environment variables exported from $ENV_FILE"
