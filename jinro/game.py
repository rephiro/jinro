# -*- coding: utf-8 -*-

import json

import common


class JinroGame(object):

    def __init__(self, users=[], admin=""):
        self.users = users
        self.admin = admin

    def end(self):
        pass

    def __repr__(self):
        return json.dumps({
            "users": self.users,
            "admin": self.admin,
        }, default=common.json_serializable_function())
