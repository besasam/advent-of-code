import json


def json_sum(decoded_json):
    s = 0
    if type(decoded_json) == list:
        for x in decoded_json:
            if type(x) == int:
                s += x
            elif type(x) == list or type(x) == dict:
                s += json_sum(x)
    elif type(decoded_json) == dict:
        for x in decoded_json:
            if type(decoded_json[x]) == int:
                s += decoded_json[x]
            elif type(decoded_json[x]) == list or type(decoded_json[x]) == dict:
                s += json_sum(decoded_json[x])
    return s


def json_sum_no_red(decoded_json):
    s = 0
    if type(decoded_json) == list:
        for x in decoded_json:
            if type(x) == int:
                s += x
            elif type(x) == list or type(x) == dict:
                s += json_sum_no_red(x)
    elif type(decoded_json) == dict:
        for x in decoded_json:
            if decoded_json[x] == 'red':
                return 0
            if type(decoded_json[x]) == int:
                s += decoded_json[x]
            elif type(decoded_json[x]) == list or type(decoded_json[x]) == dict:
                s += json_sum_no_red(decoded_json[x])
    return s


with open('input.json') as f:
    data = json.loads(f.read())


print(json_sum_no_red(data))
