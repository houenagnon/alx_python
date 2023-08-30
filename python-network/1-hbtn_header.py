#!/usr/bin/env python3
"""
This script sends a request to a given URL and displays the value of the X-Request-Id header.
Usage: python script.py <URL>
"""

import requests
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Display the X-Request-Id header if it exists
x_request_id = response.headers.get("X-Request-Id")

print(x_request_id)
