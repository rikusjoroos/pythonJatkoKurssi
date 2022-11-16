
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
        "title" : "jpk data",
        "body" : "lorem ipsun",
        "userId" : 1023
        }
        
response = requests.post(url, data = data)

print("status = ", response.status_code)
print(response.text)

