# -*- coding: utf-8 -*-

import flask
import json

import common


class Server(object):

    def __init__(self):
        self.app = flask.Flask(__name__)
        self.users = []

        @self.app.route('/', methods=['GET', 'POST'])
        def info():
            res = flask.make_response()
            res.data = str(self)
            res.headers['Content-type'] = 'text/json'
            return res

        @self.app.route('/', methods=['POST'])
        def postrequest():
            data = flask.request.data
            dict_data = json.loads(data)
            name = dict_data['name']
            res = flask.make_response()
            res.data = 'name = {name}'.format(name=name)
            res.headers['Content-type'] = 'text/plain'
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

        @self.app.errorhandler(409)
        def conflict(error):
            data = json.dumps({
                "status": 409,
                "msg": "resource conflict"
            })
            return flask.make_response(data, 409)

    def __repr__(self):
        data = {}
        data["server"] = "Jinro Server"
        data["users"] = self.users
        return json.dumps(data, default=common.support_json_serializable)


def main():
    sv = Server()
    sv.app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
