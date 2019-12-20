# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow import Schema


class User(Schema):
    firstname = fields.Str()
    middlename = fields.Str()
    lastname = fields.Str()
