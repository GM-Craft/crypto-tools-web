

import os
from loguru import logger
from tornado.options import options, define

define('port', default=8121, help='监听端口')


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    'project_path': PROJECT_PATH,
    "static_path": "static",
    "template_path": "templates",
    "debug": True,
    "cookie_secret": "bfwirmkljnweroigwcwbfhjwebfwrjufdwfewrf",
    "login_url": "/account/login",
    "xsrf_cookies": True
}

os.chdir(PROJECT_PATH)
logger.add(os.path.join(PROJECT_PATH, "log", "tornado.log"), rotation="00:00:00", retention="3 days", level="DEBUG")

options.parse_command_line()
logger.info(f'启动程序,启动端口:{options.port}')

