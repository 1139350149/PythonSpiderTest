# coding=utf-8
import requests
import json
import random
import math
import os
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from time import sleep

url1 = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
# url1 = 'https://www.baidu.com'
url2 = 'https://accounts.pixiv.net/api/login?lang=zh'


class Spider:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4277.0 Safari/537.36 Edg/87.0.658.0',
            'referer': 'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection' : 'close'
        }
        self.response = requests.get(url1)
        if self.response.status_code == 200:
            self.response.encoding = self.response.apparent_encoding
        else :
            print("麻了")
        self.post_key = ''

    def get_post_key(self):
        self.post_key = self.response.text.find('input', attrs={'name' : 'post_key'})
        print(self.response.text)
        print(self.post_key)


if __name__ == '__main__':
    spider = Spider()
    spider.get_post_key()

