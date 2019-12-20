# -*- coding: utf-8 -*-
import aiowrpr
from aiowrpr import routes

import aiohttp
from aiohttp import web

import api


if __name__ == "__main__":
    app = aiohttp.web.Application()
    app.router.add_routes(routes.ROUTE_TABLE)
    aiohttp.web.run_app(app)
