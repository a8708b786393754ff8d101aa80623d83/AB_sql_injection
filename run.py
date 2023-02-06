#! /usr/bin/python3

from sql_injection.request.request_get import RequestGet
from sql_injection.request.request_post import RequestPost

from sql_injection.form import Form

import requests, bs4 


url = 'http://192.168.0.10/dvwa/login.php'

r = requests.get(url)
soup = bs4.BeautifulSoup(r.content, 'lxml')

form = Form(soup.find('form'))

method = form.method.lower()
if method == 'get': 
    req = RequestGet(url)

elif method == 'post': 
    req = RequestPost(url)

print(req.request())

