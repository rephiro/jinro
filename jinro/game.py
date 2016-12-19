# -*- coding: utf-8 -*-

import common


class Member(common.JinroObject):

    def __init__(self, mura=0, uranai=0, reino=0, jinro=0, kyojin=0):
        self.mura = mura
        self.uranai = uranai
        self.reino = reino

        self.jinro = jinro
        self.kyojin = kyojin


class Rule(common.JinroObject):

    rules = {
        "member": "各役職の人数",
        "syoniti_kami": "初日の夜噛まれる人がいるか T/F",
    }

    def __init__(self, **member_set):
        self.member = Member(**member_set)
        self.syoniti_kami = False


class JinroGame(common.JinroObject):

    (
        created,
        playing,
        over,
    ) = (
        "created",
        "playing",
        "over",
    )

    def __init__(self, users=[], admin=None):
        self.users = users
        if admin not in users:
            raise Exception("admin user must be in participant")
        self.admin = admin
        self.rule = Rule()
        self.game_status = JinroGame.created
        self.message = "ゲームを開始してください"

    def post(self, op, args, user=None):
        if user is None:
            raise Exception('user {0} is not found'.format(user))
        method = getattr(self, 'post_{0}'.format(op))
        if not callable(method):
            raise Exception('operation {0} is not found'.format(op))
        method(args, player=user)

    def post_start(self, args, player=None):
        self.game_status = JinroGame.playing
        self.message = "初日の選択をしてください"

    def post_end(self, args, player=None):
        self.game_status = JinroGame.over
        self.message = "ゲーム終了済み"

    def ruleset(self, rule):
        pass


def main():
    from common import User
    from game import JinroGame
    admin = User('bonobono')
    g = JinroGame(
        users=[
            admin,
            User('araiguma'),
            User('shimarisu'),
            User('kuzuri'),
            User('higumanotaisyo'),
            User('fenegy'),
            User('anaguma'),
            User('shimacchau'),
        ], admin=admin)
    print("game:{0}, {1}".format(g.game_status, g.message))

    g.post("start", [], user=admin)
    print("game:{0}, {1}".format(g.game_status, g.message))

    g.post("end", [], user=admin)
    print("game:{0}, {1}".format(g.game_status, g.message))

if __name__ == '__main__':
    main()
