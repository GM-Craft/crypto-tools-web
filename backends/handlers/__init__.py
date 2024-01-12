
import os

class CAppRouter:

    routesPath = []
    routeConfig = []

    def __init__(self, basename: str = '/', desc: str='') -> None:
        self.basename = basename

    def __call__(self, url: str = '', desc: str=''):
        route = fr'{self.basename}{url}'.replace('//', '/')
        if route in self.__class__.routesPath:
            raise ValueError('路由已注册')

        def wrapper(cls):

            self.__class__.routesPath.append(route)
            self.__class__.routeConfig.append((route, cls))

            def wrapper2(*args, **kwargs):
                return cls(*args, **kwargs)
            
            return wrapper2
        return wrapper


currentDir = os.path.dirname(os.path.abspath(__file__))

for moduleName in os.listdir(currentDir):
    if not moduleName.endswith('.py'):
        continue

    if moduleName == '__init__.py':
        continue

    modulePath = os.path.join(currentDir, moduleName)

    try:
        with open(modulePath, "rb") as file:
            code = compile(file.read(), modulePath, 'exec')
            exec(code)

    except FileNotFoundError:
        print(f"Module file not found: {modulePath}")
    except Exception as e:
        print(f"Failed to execute module: {modulePath}, error: {e}")

