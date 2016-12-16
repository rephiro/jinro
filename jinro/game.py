# -*- coding: utf-8 -*-

import common


class JinroGame(common.JinroObject):

    def __init__(self, users=[], admin=None):
        self.users = users
        if admin not in users:
            raise Exception("admin user must be in participant")
        self.admin = admin

    def end(self):
        pass


def main():
    admin = common.User('bonobono')
    g = JinroGame(
        users=[
            admin,
            common.User('araiguma'),
            common.User('shimarisu'),
            common.User('kuzuri'),
            common.User('higumanotaisyo'),
            common.User('fenegy'),
            common.User('anaguma'),
            common.User('shimacchau'),
        ], admin=admin)
    print(g)


if __name__ == '__main__':
    main()
