# -*- coding: utf-8 -*-

from aiohttp.web import Request
from aiowrpr.routes import make_route

from scheme import user


@make_route(
    output_args=user.User
)
async def get_current(request: Request) -> dict:
    return {
        'firstname': 'Vasily',
        'lastname': 'Pupkin'
    }
