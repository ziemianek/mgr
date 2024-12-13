#!/bin/bash

# Function to log messages
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    log "Please source this script: source scripts/init_venv.sh"
    exit 1
fi

log "Starting virtual environment setup..."

# Check if the virtual environment already exists
if [ ! -d ".taskmgr" ]; then
    log "Virtual environment not found. Creating a new one..."
    
    # Create a Python3 virtual environment called .taskmgr
    python3 -m venv .taskmgr
    if [ $? -ne 0 ]; then
        log "Failed to create virtual environment."
        exit 1
    fi

    # Activate the virtual environment
    source .taskmgr/bin/activate
    if [ $? -ne 0 ]; then
        log "Failed to activate virtual environment."
        exit 1
    fi

    log "Installing requirements from requirements.txt..."
    # Install requirements from requirements.txt
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        log "Failed to install requirements."
        exit 1
    fi

    log "Installing Ansible collections from ansible-collections.yaml..."
    # Install Ansible collections from ansible-collections.yaml
    ansible-galaxy collection install -r ansible-collections.yaml
    if [ $? -ne 0 ]; then
        log "Failed to install Ansible collections."
        exit 1
    fi
else
    log "Virtual environment already exists. Activating it..."
    # Activate the virtual environment
    source .taskmgr/bin/activate
    if [ $? -ne 0 ]; then
        log "Failed to activate virtual environment."
        exit 1
    fi
fi

log "Virtual environment setup completed successfully."
