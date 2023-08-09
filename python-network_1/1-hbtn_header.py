#!/usr/bin/python3
#Use X-Resquest-Id in headers response"""
import requests
import sys

#Make the server request using get method
req = requests.get(sys.argv[1])

#Print of X-Request-Id attribute
print(req.headers['X-Request-Id'])
