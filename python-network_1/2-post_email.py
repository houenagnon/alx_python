#!/usr/bin/env python3
"""
This script sends a POST request to a given URL with an email parameter and displays the response body.
Usage: python script.py <URL> <email>
"""

import requests
import sys

# Get the URL and email from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Data to send in the POST request
data = {
    "email": email
}

# Send a POST request to the URL with the email parameter
response = requests.post(url, data=data)

# Display the body of the response
print(response.text)