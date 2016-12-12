# -*- coding: utf-8 -*-

import json


class User(object):

    user_serial = 0

    def __init__(self, name, password=None):
        self.name = name
        User.user_serial += 1
        self.id = User.user_serial
        self.password = password

    def __repr__(self):
        return json.dumps({
            "name": self.name,
            "id": self.id,
        })


def json_serialize_User(func):
    def wraps(*args, **kwargs):
        o = args[0]
        if isinstance(o, User):
            return json.loads(str(o))
        func(*args, **kwargs)
    return wraps


@json_serialize_User
def support_json_serializable(o):
    raise TypeError(repr(o) + " is not JSON serializable")


def main():
    u1 = User('bonobono', 'BONO')
    u2 = User('araiguma')
    print(u1)
    print(u2)


if __name__ == "__main__":
    main()
