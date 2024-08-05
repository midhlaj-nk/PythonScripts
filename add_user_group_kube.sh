#!/bin/bash

# Define the parent directory path
parent_directory="/var/snap/microk8s/"

# Check if the parent directory exists
if [ -d "$parent_directory" ]; then
    # Change permissions recursively for all files and directories
    sudo chmod -R u+rw "$parent_directory"

    # Check if the operation was successful
    if [ $? -eq 0 ]; then
        echo "Permissions updated successfully."
    else
        echo "Failed to update permissions."
    fi
else
    echo "Parent directory $parent_directory does not exist."
fi
