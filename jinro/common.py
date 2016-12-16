# -*- coding: utf-8 -*-

import json


class JinroObject(object):
    def __repr__(self):
        buf = {}
        for objname in dir(self):
            if objname.startswith("__") and objname.endswith("__"):
                continue
            obj = getattr(self, objname)
            if callable(obj):
                continue
            if objname in dir(type(self)):
                continue
            buf[objname] = obj
        return json.dumps(buf, default=json_serializable_function())


class User(JinroObject):

    user_serial = 0

    def __init__(self, name, password=None):
        self.name = name
        User.user_serial += 1
        self.id = User.user_serial
        self.password = password

    def __eq__(self, other):
        if isinstance(other, User):
            return id(self) == id(other)
        elif isinstance(other, str):
            return self.name == other
        else:
            return False


def json_serializable_function():
    from game import JinroGame

    def support_json_serializable(o):
        if isinstance(o, User) or \
                isinstance(o, JinroGame):
            return json.loads(str(o))
        raise TypeError(repr(o) + " is not JSON serializable")
    return support_json_serializable


def main():
    u1 = User('bonobono', 'BONO')
    u2 = User('araiguma')
    print(u1)
    print(u2)
    print(u1 == u1)
    print("bonobono" == u1)
    print(u1 == 'bonobono')
    print('bonobono' in [u1, u2])


if __name__ == "__main__":
    main()
