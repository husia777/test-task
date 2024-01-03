from aiohttp import web
from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()


@routes.get('/')
async def index_handler(request):
    """
    ---
    summary: Sample endpoint
    description: This is a sample endpoint.
    tags:
        - Sample
    responses:
        "200":
            description: Successful response
    """
    return web.Response(text="Hello, world")


@routes.get('/index')
async def s_handler(request):
    """
    ---
    summary: Another endpoint
    description: This is another endpoint.
    tags:
        - Another
    responses:
        "200":
            description: Successful response
    """
    return web.Response(text="Hello, world")


def init_func(argv):
    app = web.Application()
    app.add_routes(routes)
    setup_swagger(app)
    return app
