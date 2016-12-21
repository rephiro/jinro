# -*- coding: utf-8 -*-

import common


class Member(common.JinroObject):

    (
        MURA,
        URANAI,
        REINO,
        KARIUDO,
        KYOYU,

        JINRO,
        KYOJIN,

        YOKO,
    ) = (
        u"村人",
        u"占い師",
        u"霊能者",
        u"狩人",
        u"共有者",

        u"人狼",
        u"狂人",

        u"妖狐",
    )

    default_members = {
        4: {
            MURA: 1,
            URANAI: 1,
            REINO: 1,
            JINRO: 1,
        },
        5: {
            MURA: 1,
            URANAI: 1,
            KARIUDO: 1,
            JINRO: 1,
            KYOJIN: 1,
        },
        6: {
            MURA: 3,
            URANAI: 1,
            JINRO: 1,
            YOKO: 1,
        },
        7: {
            MURA: 2,
            URANAI: 1,
            REINO: 1,
            KARIUDO: 1,
            JINRO: 1,
            KYOJIN: 1,
        },
        8: {
            MURA: 1,
            URANAI: 1,
            REINO: 1,
            KYOYU: 2,
            JINRO: 2,
            KYOJIN: 1,
        },
    }

    def __init__(
            self, mura=0, uranai=0, reino=0, kariudo=0, kyoyu=0,
            jinro=0, kyojin=0, yoko=0):
        self.yaku = {
            Member.MURA: mura,
            Member.URANAI: uranai,
            Member.REINO: reino,
            Member.KARIUDO: kariudo,
            Member.KYOYU: kyoyu,

            Member.JINRO: jinro,
            Member.KYOJIN: kyojin,

            Member.YOKO: yoko,
        }

    def randomset(self, member_num):
        if member_num not in Member.default_members:
            Exception(u"{0}人用のデフォルトルールが規定されていません".format(member_num))
        template = Member.default_members[member_num]
        for yaku in template:
            self.yaku[yaku] = template[yaku]


class Rule(common.JinroObject):

    rules = {
        "member": u"各役職の人数",
        "syoniti_kami": u"初日の夜噛まれる人がいるか T/F",
    }

    def __init__(self, **member_set):
        self.member = Member(**member_set)
        self.syoniti_kami = False

    def set(self, member_num, members=None):
        if members is None:
            self.member.randomset(member_num)


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
        self.message = u"ゲームを開始してください"

    def post(self, op, args, user=None):
        if user is None:
            raise Exception('user {0} is not found'.format(user))
        method = getattr(self, 'post_{0}'.format(op))
        if not callable(method):
            raise Exception('operation {0} is not found'.format(op))
        method(args, player=user)

    def post_start(self, args, player=None):
        self.rule.set(len(self.users))
        self.game_status = JinroGame.playing
        self.message = u"初日の選択をしてください"

    def post_end(self, args, player=None):
        self.game_status = JinroGame.over
        self.message = u"ゲーム終了済み"

    def post_ruleset(self, rule):
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
    print(u"game:{0}, {1}".format(g.game_status, g.message))

    args = {}
    g.post("start", args, user=admin)
    print(u" ゲーム人数:{0}".format(len(g.users)))
    for yaku in g.rule.member.yaku:
        num = g.rule.member.yaku[yaku]
        if num != 0:
            print(u"  {yaku}: {num}".format(yaku=yaku, num=num))
    print(u"game:{0}, {1}".format(g.game_status, g.message))

    args = {}
    g.post("end", args, user=admin)
    print(u"game:{0}, {1}".format(g.game_status, g.message))


if __name__ == '__main__':
    main()
