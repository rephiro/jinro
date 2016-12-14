# -*- coding: utf-8 -*-

import json

import common


class JinroGame(object):

    def __init__(self, users=[], admin=None):
        self.users = users
        self.admin = admin

    def end(self):
        pass

    def __repr__(self):
        return json.dumps({
            "users": self.users,
            "admin": self.admin,
        }, default=common.json_serializable_function())


def main():
    u1 = common.User('bonobono')
    u2 = common.User('araiguma')
    g = JinroGame(users=[u1, u2], admin=u1)
    print(g)


if __name__ == '__main__':
    main()
