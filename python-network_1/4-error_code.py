#!/usr/bin/env python3
"""
This script sends a  request to a given URL and displays the response body.
Usage: python script.py <URL>
"""

import requests
import sys

# Get the URL and email from the command-line arguments
url = sys.argv[1]

# Send a POST request to the URL with the email parameter
response = requests.get(url)

# Display the body of the response
print(response.text)