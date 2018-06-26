BOT_NAME = 'video'

SPIDER_MODULES = ['video.spiders']
NEWSPIDER_MODULE = 'video.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'video.pipelines.VideoPipeline': 300,
}

COOKIES_ENABLED = True
DOWNLOAD_DELAY = 10
LOG_LEVEL = 'DEBUG'
RANDOMIZE_DOWNLOAD_DELAY = True
# 关闭重定向
REDIRECT_ENABLED = False
# 返回302时,按正常返回对待,可以正常写入cookie
HTTPERROR_ALLOWED_CODES = [302,]

# 伪装成浏览器访问页面
# USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

# MONGODB 主机环回地址127.0.0.1  
MONGODB_HOST = '127.0.0.1'  
# 端口号，默认是27017  
MONGODB_PORT = 27017  
# 设置数据库名称
MONGODB_DBNAME = 'MaoYan'  
# 存放本次数据的表名称  
MONGODB_DOCNAME = 'MaoYanVideos'