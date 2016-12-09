# -*- coding: utf-8 -*-

import flask
import json

import common


class Server(object):

    def __init__(self):
        self.app = flask.Flask(__name__)
        self.users = []

        @self.app.route('/', methods=['GET'])
        def getrequest():
            res = flask.make_response()
            res.data = 'Jinro Server\n'
            res.data += self.users
            res.headers['Content-type'] = 'text/plain'
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
                res.data = "{name} is already exists.".format(name=name)
                res.headers['Content-type'] = 'text/plain'
                return res
            self.users.append(common.User(name))
            res.data = json.dumps(
                self.users, default=common.support_json_serializable)
            res.headers['Content-type'] = 'text/json'
            return res


def main():
    sv = Server()
    sv.app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
