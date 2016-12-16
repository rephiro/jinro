# -*- coding: utf-8 -*-

import common


class JinroGame(common.JinroObject):

    def __init__(self, users=[], admin=None):
        self.users = users
        self.admin = admin

    def end(self):
        pass


def main():
    u1 = common.User('bonobono')
    u2 = common.User('araiguma')
    g = JinroGame(users=[u1, u2], admin=u1)
    print(g)


if __name__ == '__main__':
    main()
