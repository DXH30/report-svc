#!/usr/bin/bash

API_URL="http://localhost:5000/convert"  # Replace with your actual API URL

# Replace with the actual content you want to send
#CONTENT=$(cat example_content.txt)
CONTENT="This is the content that will be sent"

# Make a POST request to the Flask API
curl -X POST -F "content=$CONTENT" -F "email=dhs0223@gmail.com" $API_URL
