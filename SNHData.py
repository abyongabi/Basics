import json
import random

from selenium.webdriver.common import keys

f = open('Resources/MemberData.json')

data = json.load(f)
f.close()

members_dict = {}

for i in data['rows']:
    ls = [i['sname'], int(i['height']), i['birth_day'], i['star_sign_12'], i['birth_place'],
          int(i['ranking']) if i['ranking'] is not None and i['ranking'].isdigit() else -999]
    if i['tname'] not in members_dict.keys():
        members_dict[i['tname']] = [ls]
    else:
        old = members_dict[i['tname']]
        new = old + [ls]
        members_dict[i['tname']] = new

keys = list(members_dict.keys())


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


def cp():
    # for i in range(1,5):
    #     print(f"{i}. {keys[i-1]}")
    #tmemA = members_dict[keys[int(input("Enter the team of the first member: "))-1]]
    tmemA = members_dict['NII']
    #tmemB = members_dict[keys[int(input("Enter the team of the second member: "))-1]]
    tmemB = members_dict['NII']
    memA = tmemA[random.randint(0, len(tmemA) - 1)]
    memB = tmemB[random.randint(0, len(tmemB) - 1)]
    #return (memA[0], memB[0])
    return ('刘姝贤', memB[0])

l = 38
valA = []
valB = []
valC = []
b = '胡晓慧'
c = '刘姝贤'
k = 0
N = 10000
n = 1000
while k < n:
    matchA = 0
    matchB = 0
    matchC = 0
    for i in range(0,N):
        res = cp()
        if b in res and c in res:
            matchA += 1
        elif c in res and b not in res:
            matchC += 1
    valA.append(matchA/N)
    valC.append(matchC/N)
    k += 1


compA = 0
compC = 0
for i in range(0,n):
    if valA[i] > 100/3800:
        compA += 1
    if valC[i] > 100/3800:
        compC += 1
print(compA/n, compC/n)

