# -*- coding: utf-8 -*-
import aiowrpr
from aiowrpr import routes

import aiohttp
from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

import api


if __name__ == "__main__":
    app = aiohttp.web.Application()
    app.router.add_routes(routes.ROUTE_TABLE)

    setup_aiohttp_apispec(app, swagger_path="/spec", version="v1")
    aiohttp.web.run_app(app)
