import logging.handlers
import os


def log_conf():
    """初始化日志配置"""
    # 日志文件位置
    log = "./log"
    # 日志器
    logger = logging.getLogger()
    # 日志级别
    logger.setLevel(logging.INFO)
    # 处理器
    sh = logging.StreamHandler()
    # 格式化器
    fh = logging.handlers.TimedRotatingFileHandler(filename=log + os.sep + "mini.log",
                                                   when="midnight", interval=1,
                                                   backupCount=7, encoding="utf-8")
    # 格式化字符串
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)
    # 处理器添加格式化器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "033a7Oll2OyLL545rknl2uvIjD4a7Olr"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "e877898b4cea6bc5ac61e96a4b458f10"
}
