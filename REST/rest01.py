# -*- coding: utf-8 -*-

import requests

ok  = True

url ="https://v2.jokeapi.dev/joke/Programming?safe-mode"

try:
    response = requests.get(
        url,
        headers = {
            "Accept": "application/json"
            },
        params = {
            "type": "single"
            }
        )
except Exception as e:
    print(e)
    ok = False

if ok:
    data=response.json()
    print(data['joke'])