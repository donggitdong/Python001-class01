import requests
import random
from bs4 import BeautifulSoup as bs
import pandas


#1、请求猫眼页面
url = "https://www.maoyan.com/films?showType=3"

Ua_List = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0"
]



user_agent = random.choice(Ua_List)
header = {'user_agent':user_agent}

req = requests.get(url,headers=header)
print (req)
print (req.status_code)

#2、获取页面，对页面做解析,电影名称、电影类型，上映时间
#       <div class="movie-item-hover">
#         <a href="/films/1250952" target="_blank" data-act="movie-click" data-val="{movieid:1250952}">
#            <img class="movie-hover-img" src="https://p0.meituan.net/movie/ecca4f0b95340b2c57006a1bace4c3f91386100.jpg@218w_300h_1e_1c" alt="天气之子">
		   
#           <div class="movie-hover-info">
		  
#             <div class="movie-hover-title" title="天气之子">
#               <span class="name ">天气之子</span>
#                 <span class="score channel-detail-orange"><i class="integer">9.</i><i class="fraction">0</i></span>
#             </div>
			
#             <div class="movie-hover-title" title="天气之子">
#               <span class="hover-tag">类型:</span>
#               爱情／动画／奇幻
#             </div>
			
#             <div class="movie-hover-title" title="天气之子">
#               <span class="hover-tag">主演:</span>
#               醍醐虎汰朗／森七菜／本田翼
#             </div>
			
#             <div class="movie-hover-title movie-hover-brief" title="天气之子">
#               <span class="hover-tag">上映时间:</span>
#               2019-11-01
#             </div>

movie_info = bs(req.text,'html.parser')
keyitem = movie_info.find_all(class_='movie-hover-info')
print(keyitem)

#3、将获取到的页面信息提取，电影名称，电影连接，电影类型，上映时间，以utf-8的形式存入到csv文件中。
movie_list = []
for item in keyitem:
    movie_name = item.find(class_='name').text
    movie_info = item.find_all(class_='movie-hover-title')
    movie_type = movie_info[1].text.split()
    movie_time = movie_info[3].text.split()
    movie_link = item.parent.get('href')
    moive = {
        '电影名称：': movie_name,
        '电影链接：': movie_link,
        movie_type[0]: movie_type[1],
        movie_time[0]: movie_time[1]
    }
    movie_list.append(moive)


movie = pandas.DataFrame(movie_list)
movie.to_csv('./movie.csv', index=False,encoding='utf-8',header=False)

        





