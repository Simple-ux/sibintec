import requests
import time
import subprocess

url = 'http://127.0.0.1:8000'

def url_request_test(url):

    try:
        response = requests.get(url)
    except:
        subprocess.run(["docker", "restart", "app"])

    

while True:
    url_request_test(url)
    time.sleep(5)

