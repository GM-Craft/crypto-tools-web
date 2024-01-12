

import asyncio
from tornado.web import Application
from tornado.options import options

import config
from handlers import CAppRouter


async def main():
    app = Application(CAppRouter.routeConfig, **config.SETTINGS)
    app.listen(options.port)
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())
