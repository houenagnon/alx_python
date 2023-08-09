#!/usr/bin/python3
""" sends a POST request to the passed URL with the email 
as a parameter, and finally displays the body of the response"""

import requests
import sys

#Make the server request using get method
req = requests.post(sys.argv[1], data={"email":sys.argv[2]})

#Print of X-Request-Id attribute
print(req.content)
