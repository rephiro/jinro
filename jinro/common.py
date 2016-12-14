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

    def __eq__(self, other):
        if isinstance(other, User):
            return self == other
        elif isinstance(other, str):
            return self.name == other
        else:
            return False


def json_serializable_function():
    from game import JinroGame

    def support_json_serializable(o):
        if isinstance(o, User):
            return json.loads(str(o))
        if isinstance(o, JinroGame):
            return json.loads(str(o))
        raise TypeError(repr(o) + " is not JSON serializable")
    return support_json_serializable


def main():
    u1 = User('bonobono', 'BONO')
    u2 = User('araiguma')
    print(u1)
    print(u2)
    print(u1 == 'bonobono')
    print('bonobono' in [u1, u2])


if __name__ == "__main__":
    main()
