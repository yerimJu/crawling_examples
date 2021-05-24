import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)

'''
$ python req-client_info.py
[ip]
API_URI=http://api.aoikujira.com/ip/get.php
REMOTE_ADDR=27.122.242.78
REMOTE_HOST=27.122.242.78
REMOTE_PORT=53294
HTTP_HOST=api.aoikujira.com
HTTP_USER_AGENT=Python-urllib/3.8
HTTP_ACCEPT_LANGUAGE=
HTTP_ACCEPT_CHARSET=
SERVER_PORT=80
FORMAT=ini
'''