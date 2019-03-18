import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "http://www.weather.com.cn/textFC/hb.shtml"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 "
                 "Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"
}
response = requests.get(url, headers=headers)
text = response.content.decode("utf-8")
soup = BeautifulSoup(text,"lxml")
# table = soup.find("div",class_="lqcontentBoxH").find("div",class_="contentboxTab").find("div",class_="contentboxTab1").find("div",class_="contentboxTab2")
# day_tabs = table.find("url",class_="day_tabs")
table_1s = soup.find_all("table")
list1 = []
for table_1 in table_1s:
    trs = table_1.find_all("tr")[2:]
    for index,tr in enumerate(trs):
        tds = tr.find_all("td")
        if index==0:
            province = list(tds[0].stripped_strings)[0]
            city = list(tds[1].stripped_strings)[0]
            high_temp = list(tds[4].stripped_strings)[0]
            cloud = list(tds[5].stripped_strings)[0]
            low_temp = list(tds[-2].stripped_strings)[0]
            list1.append({"province":province,"city":city, "high_temp":high_temp, "cloud":cloud, "low_temp":low_temp})
        else:
            city = list(tds[0].stripped_strings)[0]
            high_temp = list(tds[3].stripped_strings)[0]
            cloud = list(tds[4].stripped_strings)[0]
            low_temp = list(tds[-2].stripped_strings)[0]
            list1.append({"province": province, "city": city, "high_temp": high_temp, "cloud": cloud, "low_temp": low_temp})
        province = province

print(list1)
column = ['province','city','high_temp','cloud','low_temp']
weather = pd.DataFrame(data=list1, columns=column)
weather.to_csv('华北地区天气.csv', index=False,encoding='gb2312')






















#1.报错：AttributeError: 'NoneType' object has no attribute 'find'
#  因为 tables 获取的数据类型为空类型“NoneType”，我们可以使用isinstance将空类型过滤掉：
#   tables = soup.find("div",class_="lqcontentBoxH")
#   if isinstance(tables, bs4.element.Tag):
#       print(tables)