#!/bin/bash

script_name="pushToremoteDatabase.py"

# Check if the script is running
if pgrep -f "$script_name" > /dev/null; then
    echo "$script_name is running."
else
    echo "$script_name is not running."
fi
