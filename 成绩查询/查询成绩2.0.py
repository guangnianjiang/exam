import requests
from bs4 import BeautifulSoup
import re

url_login='http://222.188.0.101/loginAction.do'
url_cj='http://222.188.0.101/bxqcjcxAction.do'
url_yz='http://222.188.0.101/menu/s_top.jsp'
headers={
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#input("请输入账号：")
zjh=input("请输入账号：")
#input("请输入密码：")
mm=input("请输入密码：")

datas={
    'zjh': zjh,
    'mm': mm
}

session=requests.session()
html=session.post(url=url_login,headers=headers,data=datas)
cookies=requests.utils.dict_from_cookiejar(session.cookies)

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID='+cookies['JSESSIONID'],
    'Host': '222.188.0.101',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

html_yz=requests.get(url=url_yz,headers=headers)
soup=BeautifulSoup(html_yz.text,'html.parser')
name_string=soup.find_all('table',align='right',border="0",cellpadding="0",cellspacing="0",class_="leftuser01")
name=name_string[0].text.strip()[5:8]
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID='+cookies['JSESSIONID'],
    'Host': '222.188.0.101',
    'Referer': 'http://222.188.0.101/menu/s_menu.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

html_cj=requests.get(url=url_cj,headers=headers)

soup=BeautifulSoup(html_cj.text,'html.parser')
t=soup.find_all('tr',class_='odd')
print(name+' 您的成绩如下：')
for i in t:
    subject=i.find_all('td')[2].string
    score=i.find_all('td')[6].string
    print(subject.strip()+'----'+score.strip())
        
raw=input("Press <enter>")
