
import os
from collections import defaultdict

from tornado.web import Application



class CAppRouter:
    '''
    basename 和 url 要么为空，要么以 / 开头
    '''
    routedict = defaultdict()

    def __init__(self, basename: str = '/', desc: str='') -> None:
        if basename in self.__class__.routedict:
            raise ValueError(f'{basename}键已存在, 路由已注册')

        self.basename = basename

    def __call__(self, url: str = '', desc: str=''):
        if self.__class__.routedict.get(self.basename) and \
                url in [item[0] for item in self.__class__.routedict.get(self.basename).values()]:
            raise ValueError(f'路由已注册')

        def wrapper(cls):
            if not self.__class__.routedict.get(self.basename):
                self.__class__.routedict[self.basename] = {}

            self.__class__.routedict[self.basename][url] = (fr'{self.basename}{url}'.replace('//', '/'), cls)

            def wrapper2(*args, **kwargs):
                return cls(*args, **kwargs)

            return wrapper2

        return wrapper

    @staticmethod
    def registerRoutes(app: Application):
        app.add_handlers(".*$", CAppRouter.routes())

    @staticmethod
    def routes():
        routers = []
        for base in CAppRouter.routedict.values():
            for route in base.values():
                routers.append(route)
        return routers


current_dir = os.path.dirname(os.path.abspath(__file__))

for module_name in os.listdir(current_dir):
    if not module_name.endswith('.py'):
        continue

    if module_name == '__init__.py':
        continue

    module_path = os.path.join(current_dir, module_name)

    try:
        with open(module_path, "rb") as file:
            code = compile(file.read(), module_path, 'exec')
            exec(code)

    except FileNotFoundError:
        print(f"Module file not found: {module_path}")
    except Exception as e:
        print(f"Failed to execute module: {module_path}, error: {e}")

