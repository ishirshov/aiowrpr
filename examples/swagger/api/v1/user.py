# -*- coding: utf-8 -*-

from aiohttp.web import Request
from aiowrpr.routes import make_route

from scheme import user


@make_route(
    input_args=user.User,
    output_args=user.User
)
async def format(request:Request, **kwargs) -> dict:
    """
    Capitalizes the user values such as Firstname, Lastname and Middlename.
    """

    return {
        'firstname': kwargs['firstname'].capitalize(),
        'middlename': kwargs['middlename'].capitalize(),
        'lastname': kwargs['lastname'].capitalize(),
    }


@make_route(
    output_args=user.User
)
async def get_current(request: Request) -> dict:
    return {
        'firstname': 'Vasily',
        'lastname': 'Pupkin'
    }
