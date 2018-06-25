# Spider

1. 环境要求
> 安装Python  
安装scrapy库：conda install scrapy  
安装pymongo库：conda install scrapy  
安装MongoDB  

2. 执行
爬取猫眼电影：在maoyan目录下，运行指令
```
scrapy crawl maoyan
```
爬去豆瓣电影TOP250：在douban250目录下，运行指令
```
scrapy crawl douban250
```

3. 结果
将爬取的结果写入MongoDB中

豆瓣电影存储格式： 

|database|DouBan|  
|:-: | :-: |
| collections | DouBanMovies |
| id | id |
| title | 电影名字 |
| director | 导演 |
| actor | 演员 |
| year| 年份|
| country | 国家 |
| type |电影类型 |
| rating_num |豆瓣评分 |
| quote | 经典台词 |
| image | 电影剧照URL|

*所有的值都存储为String格式*

猫眼电影存储格式：

|database|MaoYan|  
|:-: | :-: |
| collections | MaoYanMovies |
| id | id |
| movie_name | 电影名字 |
| movie_ename | 电影英文名字 |
| movie_type | 电影类型 |
| country | 国家 |
| movie_time | 电影时长 |
| online_time | 电影上映时间 |
| movie_star | 评分 |
| movie_total_price | 票房 |
| img | 电影剧照URL|
| director | 导演 |
| director_src | 导演照片URL |
| actor | 演员 |
| actor_src | 演员照片URL |
| introduction | 经典台词 |

*actor及actor的值存储为Array, 其他值均存储为String*
*由于猫眼的电影的评分数据及票房数据均采用加密，爬取下来的数据均为乱码*

4. Robo 3T GUI工具
豆瓣电影的第一项，如下图所示：

猫眼电影的第一项，如下图所示：

