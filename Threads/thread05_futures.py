# -*- coding: utf-8 -*-

import threading
import requests
import concurrent.futures as cf

def get_wiki_page_existence(wiki_page_url, timeout= 10):
    response = requests.get(url=wiki_page_url, timeout = timeout)
    
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"
    

    return wiki_page_url + " - " + page_status

wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/doesnotexist",
    "https://en.wikipedia.org/wiki/Shark"
    ]

futures = []

with cf.ThreadPoolExecutor() as executor:
    for url in wiki_page_urls:
        f = executor.submit(get_wiki_page_existence, wiki_page_url = url)
        futures.append(f)
    
for f in cf.as_completed(futures):
    print(f.result())


