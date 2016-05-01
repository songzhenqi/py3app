# coding: utf-8
import requests

url = "http://119.146.201.171:8090/dologin.action"
param = {"os_username": "songzhenqi", "os_password": "123456"}
r = requests.post(url, data=param)
print(r.text)
