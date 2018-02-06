import requests
import re

login = 'http://eamis.nankai.edu.cn/eams/login.action'
grade = 'http://eamis.nankai.edu.cn/eams/myPlanCompl.action'
username = input('用户名：')
password = input('密  码：')

data = {'username': username, 'password': password, 'session_locale': 'zh_CN'}

s = requests.Session()  # 保存Cookies
s.post(login, data = data)  # 模拟登陆

t = s.get(grade).text  # 提取网页源代码

targets = re.findall('10%.*?<td>(.*?)<.*?">.*?<.*?">(.*?)<.*?">(.*?)\s*?<', t, re.S)  # (name, credits, grade)
name = re.search('姓名.*?">(.*?)<', t, re.S).group(1)

sum = 0.0
target = 0.0

for tuple in targets:
    if tuple[2] not in ['--', '', '通过']:
        sum += float(tuple[1])
        target += float(tuple[1]) * float(tuple[2])

target /= sum

print (name, ':', target)
