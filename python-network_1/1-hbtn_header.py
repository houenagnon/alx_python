#!/usr/bin/python3
"""Use X-Resquest-Id in headers response"""
import requests
import sys

req = requests.get(sys.argv[1])

print(req.headers['X-Request-Id'])
