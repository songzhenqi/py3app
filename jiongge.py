# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

__author__ = 'User'

baseUrl = "http://www.52rkl.cn/jiongge/"
html = urlopen(baseUrl)
bsObj = BeautifulSoup(html, "html.parser")

subList = bsObj.find_all("article")
for link in subList:
    print(link)

# print(bsObj.prettify())
