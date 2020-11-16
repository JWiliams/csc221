#!/usr/bin/env python3

'''Link verification

Author: Javian Williams

'''
import argparse
import requests
import bs4
import os

'''Given a URL of a web page, attempt to download every linked
page on the page. Flag any pages that have a 404 "Not Found"
status code and print them out as broken links.
Args:
 url (str): URL to crawl and verify

Returns:
  None
  '''
# Place solution in this funtion
url ='https://nostarch.com/automatestuff2/'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linksList = soup.find_all('a')
links = []
for link in linksList:
    if 'href' in link.attrs:
        a=(link.attrs['href']).split('\n')
        for line in a: 
            linkUrl = 'nostarch.com' + str(line)
            links.append(linkUrl)
print(links)
