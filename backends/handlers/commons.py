

from loguru import logger
from tornado.web import RequestHandler

from . import CAppRouter


index = CAppRouter('', desc='首页等常用页')

@index('/')
class IndexPage(RequestHandler):
    def get(self):

        self.render('index.html')
