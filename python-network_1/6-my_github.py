#!/usr/bin/env python3
import requests
import sys

def get_user_id(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        return user_id
    else:
        print(f"Error: Unable to retrieve user data (Status Code: {response.status_code})")
        return None

if len(sys.argv) < 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]
user_id = get_user_id(username, token)

if user_id is not None:
    print(f"{user_id}")
