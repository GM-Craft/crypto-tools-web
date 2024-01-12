

from loguru import logger
from tornado.web import RequestHandler

from . import CAppRouter


index = CAppRouter('')

@index('/')
class IndexPage(RequestHandler):
    def get(self):
        logger.info('index page')
        self.render('index.html')


@index('/next')
class IndexPage2(RequestHandler):
    def get(self):
        logger.info('index page')
        self.write('hello')
