#!/usr/bin/bash

API_URL="http://localhost:5000/convert"  # Replace with your actual API URL

# Replace with the actual content you want to send
CONTENT=$(cat example_content.txt)

# Set the environment variable for the forward API URL
export FORWARD_API_URL="https://example.com/forward-api"

# Make a POST request to the Flask API
curl -X POST -F "content=$CONTENT" $API_URL
