#!/bin/bash

# Function to show usage information
usage() {
    echo "Usage: $0 --source=<source_file> --destination=<destination_file> --period=<seconds>"
    exit 1
}

# Parse command-line arguments
for arg in "$@"; do
    case $arg in
        --source=*)
            SOURCE="${arg#*=}"
            shift
            ;;
        --destination=*)
            DESTINATION="${arg#*=}"
            shift
            ;;
        --period=*)
            PERIOD="${arg#*=}"
            shift
            ;;
        *)
            usage
            ;;
    esac
done

# Validate inputs
if [[ -z "$SOURCE" || -z "$DESTINATION" || -z "$PERIOD" ]]; then
    usage
fi

if [[ ! -f "$SOURCE" ]]; then
    echo "Error: Source file does not exist."
    exit 1
fi

if ! [[ "$PERIOD" =~ ^[0-9]+$ ]]; then
    echo "Error: Period must be a positive integer."
    exit 1
fi

# Log file location
LOG_FILE="/tmp/file_sync.log"

echo "Starting file sync: '$SOURCE' -> '$DESTINATION' every $PERIOD seconds" | tee -a "$LOG_FILE"

# Run sync in the background
{
    while true; do
        TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
        if cp "$SOURCE" "$DESTINATION"; then
            echo "[$TIMESTAMP] Copy successful" >> "$LOG_FILE"
        else
            echo "[$TIMESTAMP] Copy failed" >> "$LOG_FILE"
        fi
        sleep "$PERIOD"
    done
} & disown

echo "Sync process started in the background. Logs are stored in: $LOG_FILE"
