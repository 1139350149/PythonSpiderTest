# coding=utf-8
import requests
from bs4 import BeautifulSoup


def spider_test():
    url = 'https://www.ivsky.com/bizhi/naruto_t563'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87"
                      " Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        html = BeautifulSoup(response.text, 'lxml')
        target_ul = html.find('ul', class_='il')
        target_img = target_ul.find_all('img')
        path = 'J:\\Py_Program\\SpiderTest\\template'
        count = 0
        for src in target_img:
            net_path = "http:" + (src['src'].replace('downloadpic', 'img').replace('t', 'pic').replace('img', 'downloadpic', 1) + '?download')
            name = src['alt'] + str(count) + '.jpg'
            count += 1
            file_path = path + '\\' + name
            print(file_path)
            print(net_path)
            try:
                res = requests.get(net_path, headers=headers)
                file = open(file_path, 'wb')
                file.write(res.content)
                file.close()
            except:
                print("麻了")


if __name__ == '__main__':
    spider_test()
