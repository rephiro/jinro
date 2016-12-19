# -*- coding: utf-8 -*-

import json


class JinroObject(object):

    def __repr__(self):
        buf = {}
        for objname in dir(self):
            if objname in dir(type(self)):
                continue
            obj = getattr(self, objname)
            if callable(obj):
                continue
            if objname == "repr_ng_words":
                continue
            if objname.startswith("__") and objname.endswith("__"):
                continue
            buf[objname] = obj
        if "repr_ng_words" in dir(self):
            repr_ng_words = getattr(self, "repr_ng_words")
            if isinstance(repr_ng_words, list):
                for ngword in repr_ng_words:
                    buf.pop(ngword)
        return json.dumps(buf, default=json_serializable_function())


class User(JinroObject):

    user_serial = 0
    repr_ng_words = ["password"]

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
    from game import Rule
    from game import Member
    json_serializable_class = [
        User,
        JinroGame,
        Rule,
        Member,
    ]

    def support_json_serializable(o):
        for c in json_serializable_class:
            if isinstance(o, c):
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
