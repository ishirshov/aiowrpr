# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow import Schema


class User(Schema):
    firstname = fields.Str(required=True)
    middlename = fields.Str(missing=str())
    lastname = fields.Str(required=True)
