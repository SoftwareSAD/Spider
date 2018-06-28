BOT_NAME = 'douban250'

SPIDER_MODULES = ['douban250.spiders']
NEWSPIDER_MODULE = 'douban250.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {  
   'douban250.pipelines.Douban250Pipeline': 300,  
}
# 1为该Pipeline的优先级，越小就越先执行  

# 伪装成浏览器访问页面
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"

# MONGODB 主机
MONGODB_HOST = 'ds117691.mlab.com'  
# 端口号 
MONGODB_PORT = 17691 
# 设置数据库名称
MONGODB_DBNAME = 'maoyanmovie'
# 存放本次数据的表名称  
MONGODB_DOCNAME = 'DouBan250'
# 数据库的用户名
MONGODB_USERNAME = 'heygrandpa'
# 数据库的密码
MONGODB_PASSWORD = 'SYSU2018'