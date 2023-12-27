from aiohttp import web


def init_func(argv):
    app = web.Application()
    app.router.add_get("/", index_handler)
    return app
