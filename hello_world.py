# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

wiki_base_url = "http://en.wikipedia.org"
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd="123456", db='mysql', charset="utf8")
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO pages(title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()


def get_links(article_url):
    html = urlopen(wiki_base_url + article_url)
    bsobj = BeautifulSoup(html, "html.parser")
    title = bsobj.find("h1", {"id": "firstHeading"}).get_text()
    content = bsobj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = get_links("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = get_links(newArticle)
finally:
    cur.close()
    conn.close()
