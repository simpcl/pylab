#!/usr/bin/env python3

import requests
from requests import Session
import re
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

class SimpleSpider:
    def __init__(self, timeout = 10):
        self.timeout_ = timeout

    def request_get(self, url):
        session = Session()
        resp =  session.get(url, timeout = self.timeout_)
        return resp

    def get_page_url(self, page):
        pass

    def for_each_page(self, start_page, end_page):
        for page in range(start_page, end_page):
            url = self.get_page_url(page)
            resp = self.request_get(url)
            self.process(page, resp)

    def process(self, page, resp):
        pass

class KSFan(SimpleSpider):
    def __init__(self):
        super().__init__(20)

    def get_page_url(self, page):
        url_tmpl = 'https://ksfan.net/story/kai-shu-san-guo-yan-yi/?page='
        return url_tmpl + str(page)

    def get_title(self, text):
        s = text.split('.')[0]
        ary = s.split('-')
        return ary[1].strip() + '.' + ''.join(ary[0].split(' '))
    
    def get_audio_url(self, text):
        lines = text.splitlines()
        for line in lines:
            pos = line.find("/xaud/")
            if pos > 0:
                s = line.split("'")[1]
                return 'https://ksfan.net' + s

    def process(self, page, resp):
        #print(resp.text)
        #soup = BeautifulSoup(resp.text, "lxml")
        soup = BeautifulSoup(resp.text, 'html.parser')
        div_container = soup.select('body > div.page-body > div.page-main > main.markdown-body > div.container')[0]
        h5 = div_container.select('h5')[0]
        title = self.get_title(h5.get_text())
        print(title)
        script = div_container.select('script')[0]
        print(script)
        audio_url = self.get_audio_url(script.get_text())
        print(audio_url)
        page_url = self.get_page_url(page)
        print(page_url)
        print("curl -H 'User-Agent: {user_agent}' -H 'Referer: {page_url}' -o {title}.mp3 '{audio_url}'".format(user_agent=USER_AGENT, page_url=page_url, audio_url=audio_url, title=title))

if __name__ == '__main__':
    ksfan = KSFan()
    ksfan.for_each_page(368, 369)

