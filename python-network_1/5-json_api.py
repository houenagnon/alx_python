#!/usr/bin/env python3
"""
This script sends a posts request to http://0.0.0.0:5000/search_user and displays the response body.
Usage: python script.py <URL>
"""

import requests
import sys

def search_user_by_letter(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}
    response = requests.post(url, data=params)

    try:
        response_json = response.json()
        if response_json:
            user_id = response_json.get('id')
            user_name = response_json.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user_by_letter(letter)
