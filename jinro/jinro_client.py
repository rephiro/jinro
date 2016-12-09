# -*- coding: utf-8 -*-

import urllib
import urllib2
import json


def main():
    url = 'http://localhost:8080/user'
    header = {"Content-Type": "text/json"}
    dict_data = {
        'name': 'papa',
        'operation': 'sanka',
    }
    params = urllib.urlencode({'p1': 1, 'p2': 2})
    json_data = json.dumps(dict_data)
    req = urllib2.Request(
        '{url}?{params}'.format(url=url, params=params),
        data=json_data, headers=header)
    res = urllib2.urlopen(req)
    print(res.read())


if __name__ == "__main__":
    main()
