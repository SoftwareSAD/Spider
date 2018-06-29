BOT_NAME = 'rowpiece'

SPIDER_MODULES = ['rowpiece.spiders']
NEWSPIDER_MODULE = 'rowpiece.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True
DOWNLOAD_DELAY = 10
LOG_LEVEL = 'DEBUG'
RANDOMIZE_DOWNLOAD_DELAY = True
# 关闭重定向
REDIRECT_ENABLED = False
# 返回302时,按正常返回对待,可以正常写入cookie
HTTPERROR_ALLOWED_CODES = [302,]

ITEM_PIPELINES = {
    'rowpiece.pipelines.RowpiecePipeline': 300,
}

# 伪装成浏览器访问页面
# USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

# MONGODB 主机
MONGODB_HOST = 'ds117691.mlab.com'  
# 端口号，默认是27017  
MONGODB_PORT = 17691
# 设置数据库名称
MONGODB_DBNAME = 'maoyanmovie'
# 存放本次数据的表名称  
MONGODB_DOCNAME = 'rowpiece'
# 数据库的用户名
MONGODB_USERNAME = 'heygrandpa'
# 数据库的密码
MONGODB_PASSWORD = 'SYSU2018'