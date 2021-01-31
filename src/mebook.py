#!/usr/bin/python

import requests
from requests import Session
from bs4 import BeautifulSoup
import re

url_tmpl = 'http://mebook.cc/category/hjzy/gfzy'

def get_url(page):
    if page == 1:
        return url_tmpl
    return url_tmpl + '/page/' + str(page)

def request_get(url):
    session = Session()
    resp =  session.get(url, timeout = 10)
    return resp

def list_urls(start_page, end_page):
    for page in range(start_page, end_page):
        url = get_url(page)
        resp = request_get(url)
        soup = BeautifulSoup(resp.text, "lxml")
        for li in soup.select('body > div#container > div#container-inner > div#primary > ul.list > li'):
            #print li
            a = li.select('div.content > h2 > a')
            href = a[0]['href']
            download_id = re.search('(\w+).html', href).group(1)
            download_url = 'http://mebook.cc/download.php?id=' + download_id
            #print download_url
            get_baidu_url(download_url)

def get_baidu_url(url):
    print url,
    try:
        resp = request_get(url)
        soup = BeautifulSoup(resp.text, "lxml")
        desc_p = soup.select('body > div.desc > p')
        s = desc_p[5].string
        code = s.split()[0][-4:]
        list_a = soup.select('body > div.list > a')
        baidu_url = list_a[0]['href']
        print baidu_url, code, desc_p[0].string
    except:
        print 'get_baidu_url failed'

if __name__ == '__main__':
    #get_baidu_url('http://mebook.cc/download.php?id=18644')
    #for page in xrange(40):
    #    print get_url(page + 1)
    list_urls(1, 25)

