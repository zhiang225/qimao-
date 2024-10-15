import requests
from bs4 import BeautifulSoup

# 单页小说下载的功能
def downloadPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') # BeautifulSoup(响应数据包内容，解析器)

    title = soup.find('h2', class_='chapter-title').get_text() # 拿到标题
    page1 = title + '.txt'

    list_conn = soup.find_all('div', class_='article') # 拿到小说
    for e in list_conn:
        with open(page1, 'w+') as f:
            print(f"【+】当前正在下载{page1}")
            f.write(str(e.text))

# 批量爬取小说
num = input("【+】请输入你要爬取多少章节的小说：")
num = int(num) - 1
url = "https://www.qimao.com/shuku/149774-317"
if num == 0:
    downloadPage('https://www.qimao.com/shuku/149774-316193/')
else:
    downloadPage('https://www.qimao.com/shuku/149774-316193/')
    for i in range(271,271+num):
        r = requests.get(url + str(i) + "/", timeout=5)
        if r.status_code == 200:
            downloadPage(url + str(i) + "/")
        else:
            print("【-】小说章节无法下载...")