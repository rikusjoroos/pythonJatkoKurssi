# -*- coding: utf-8 -*-

import threading
import requests

def get_wiki_page_existence(wiki_page_url, timeout= 10):
    response = requests.get(url=wiki_page_url, timeout = timeout)
    
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"
    
    global th_res_lock
    
    with th_res_lock:
        th_res[wiki_page_url] = wiki_page_url + " - " + page_status

wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/doesnotexist",
    "https://en.wikipedia.org/wiki/Shark"
    ]


th_list = []
th_res = {}
th_res_lock = threading.Lock()

for url in wiki_page_urls:
    th = threading.Thread(target = get_wiki_page_existence, args = (url,))
    th_list.append(th)
    th.start()
    
for th in th_list:
    th.join()
with th_res_lock:
    for res in th_res.values():
        print(res)


