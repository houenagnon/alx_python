#!/usr/bin/env python3
"""
This script sends a posts request to http://0.0.0.0:5000/search_user and displays the response body.
Usage: python script.py <URL>
"""

import requests
import sys

# Get the letter from the command-line arguments
q = sys.argv[1]

if q == " ":
    q = " "

# Send a POST request 

response = requests.post("http://0.0.0.0:5000/search_user", data=q)


# Display the body of the response
print(response.text)