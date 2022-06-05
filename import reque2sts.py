import requests
import time
from bs4 import BeautifulSoup
name = input()
URL_TEMPLATE = f"https://codeforces.com/api/user.status?handle={name}&from=1&count=10000"
r = requests.get(URL_TEMPLATE)
a = r.text
print(a.count("problem"))
time.sleep(5)