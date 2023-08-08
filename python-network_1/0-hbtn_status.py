#!/usr/bin/python3
import requests

req = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print(end="        ")
print("- type:", type(req.text))
print(end="        ")
print("- content:", req.text )             