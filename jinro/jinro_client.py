# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(
        description="jinro client")
    parser.add_argument(
        "-r", "--resource",
        dest="resource",
        type=str,
        default="",
        help="resource uri",
        metavar="RESOURCE_NAME")
    parser.add_argument(
        "-u", "--user",
        dest="user",
        type=str,
        default="bonobono",
        help="user name",
        metavar="USER")
    parser.add_argument(
        "-m", "--method",
        dest="method",
        type=str,
        default="GET",
        help="http method",
        metavar="METHOD")
    parser.add_argument(
        "-o", "--operation",
        dest="operation",
        type=str,
        default="create",
        help="operation to resource",
        metavar="OP")
    args = parser.parse_args()
    return args


def main():
    args = arg_parse()
    url = 'http://localhost:8080/{resource}'.format(resource=args.resource)
    header = {"Content-Type": "text/json"}
    dict_data = {
        'name': args.user,
        'operation': args.operation,
        'args': {}
    }
    params = urllib.urlencode({'p1': 1, 'p2': 2})
    json_data = json.dumps(dict_data)
    req = urllib2.Request(
        '{url}?{params}'.format(url=url, params=params),
        data=json_data,
        headers=header)
    req.get_method = lambda: args.method
    res = urllib2.urlopen(req)

    print(res.read())


if __name__ == "__main__":
    main()
