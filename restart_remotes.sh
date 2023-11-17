#!/bin/bash

script_name="pushToremoteDatabase.py"

# Kill the existing process
pkill -f "$script_name"

# Wait for 10 seconds
sleep 20

# Run the script again
python3 "$script_name" > output.log 2>&1 &