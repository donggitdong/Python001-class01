作业一：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

1、请求目标(maoyan猫眼电影)
2、点击获取电影名称、电影类型、上映时间
3、保存第二步中获取到的信息以utf-8字符集保存到csv格式的文件中

编码思路：
1、需求分析
2、代码编写
3、代码run运行起来
4、代码逻辑bug修复优化


作业二：
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址： https://maoyan.com/films?showType=3
要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。