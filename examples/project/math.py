# -*- coding: utf-8 -*-
import aiowrpr
from aiowrpr import routes

import aiohttp
from aiohttp import web

from marshmallow import fields


@aiowrpr.routes.make_route(
    input_args={
        'a': fields.Int()
    },
    output_args={
        'b': fields.Int()
    }
)
async def pow2(a: int, request: web.Request) -> int:
    return a ** 2
