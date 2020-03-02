# GPA_Calculator

自制 南开大学GPA计算器

## 原理

输入用户名密码

用requests库模拟登陆

直接在 <http://eamis.nankai.edu.cn/eams/myPlanCompl.action> 上爬取学分和成绩

计算出学分绩（百分制）

## 使用方法

1 安装 Python

2 安装 requests 包

3 在命令行中，跳转到 GPA_Calculator.py 的所在目录，输入 `python GPA_calculater.py`

4 即可显示以（‘`课程名`,'`学分`','`成绩`')为格式的列表，以及平均学分绩
