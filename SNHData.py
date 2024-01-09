import json

from selenium.webdriver.common import keys

f = open('Resources/MemberData.json')

data = json.load(f)
f.close()

members_dict = {}

for i in data['rows']:
    ls = [i['sname'], int(i['height']), i['birth_day'], i['star_sign_12'], i['birth_place'], int(i['ranking']) if i['ranking'] is not None and i['ranking'].isdigit() else -999]
    if i['tname'] not in members_dict.keys():
        members_dict[i['tname']] = [ls]
    else:
        old = members_dict[i['tname']]
        new = old + [ls]
        members_dict[i['tname']] = new

keys = members_dict.keys()
def dict_to_dict(keys, dict):
    res = {}
    for key in keys:
        group = dict[key]
        for member in group:
            if member[-1] > 0:
                if key not in res:
                    res[key] = [member]
                else:
                    res[key] = res[key] + [member]
    return res

top48 = dict_to_dict(keys, members_dict)



