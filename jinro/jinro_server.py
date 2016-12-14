# -*- coding: utf-8 -*-

import flask
import json

import common
import game


class Server(object):

    def __init__(self):
        self.app = flask.Flask(__name__)
        self.users = []
        self.game = None

        @self.app.route('/', methods=['GET', 'POST'])
        def info():
            res = flask.make_response()
            res.data = json.dumps(json.loads(str(self)), indent=2)
            res.headers['Content-type'] = 'text/json'
            return res

        @self.app.route('/game', methods=['POST'])
        def create_game():
            data = flask.request.data
            dict_data = json.loads(data)
            name = dict_data['name']
            self.game = game.JinroGame(users=self.users, admin=name)

            res = flask.make_response()
            res.data = str(self.game)
            res.headers['Content-type'] = 'text/json'
            return res

        @self.app.route('/game', methods=['DELETE'])
        def end_game():
            self.game.end()
            self.game = None

            res = flask.make_response()
            res.data = str(self.game)
            res.headers['Content-type'] = 'text/json'
            return res

        @self.app.route('/user', methods=['POST'])
        def user():
            data = flask.request.data
            dict_data = json.loads(data)
            name = dict_data['name']
            res = flask.make_response()
            if name in [u.name for u in self.users]:
                flask.abort(409)
            new_user = common.User(name)
            self.users.append(new_user)
            res.data = str(new_user)
            res.headers['Content-type'] = 'text/json'
            return res

        @self.app.route('/user/<string:username>', methods=['GET'])
        def user_get(username):
            for u in self.users:
                if u.name == username:
                    return flask.make_response(str(u))
            flask.abort(404)

        @self.app.errorhandler(409)
        def conflict(error):
            data = json.dumps({
                "status": 409,
                "msg": "resource conflict"
            })
            return flask.make_response(data, 409)

        @self.app.errorhandler(404)
        def not_found(error):
            data = json.dumps({
                "status": 404,
                "msg": "resource is not found"
            })
            return flask.make_response(data, 404)

    def __repr__(self):
        data = {
            "server": "Jinro Server",
            "users": self.users,
            "game": self.game,
        }

        return json.dumps(data, default=common.json_serializable_function())


def main():
    sv = Server()
    sv.app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
