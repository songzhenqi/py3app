#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def get_internal_links(bs_obj, include_url):
    internal_links = []
    # Finds all links that begin with a "/"
    for link in bs_obj.findAll("a", href=re.compile("^(/|.*"+include_url+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                internal_links.append(link.attrs['href'])
    return internal_links


# Retrieves a list of all external links found on a page
def get_external_links(bs_obj, exclude_url):
    external_links = []
    # Finds all links that start with "http" or "www" that do
    # not contain the current URL
    for link in bs_obj.findAll("a", href=re.compile("^(http|www)((?!"+exclude_url+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])
    return external_links


def split_address(address):
    address_parts = address.replace("http://", "").split("/")
    return address_parts


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bsobj = BeautifulSoup(html)
    external_links = get_external_links(bsobj, split_address(starting_page)[0])
    if len(external_links) == 0:
        internal_links = get_internal_links(bsobj, starting_page)
        return get_external_links(bsobj, internal_links[random.randint(0, len(internal_links)-1)])
    else:
        return external_links[random.randint(0, len(external_links)-1)]


def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print("Random external link is: " + external_link)
    follow_external_only(external_link)

follow_external_only("http://oreilly.com")
