from random import randint
from random import choice
import json
import re

# 1
def generate_random_add(country_, city_, fname):
    country = country_ + ', '
    city = 'г. ' + city_ + ', '
    adressDict = read_json_from_the_file(fname)
    for curStreet in adressDict:
        if not validate_streets(adressDict[curStreet]):
            raise Exception(f"The data format in source file is wrong in record {adressDict[curStreet]}")
    while True:
        current_Numbers = ran_numbers(adressDict)
        streetName = adressDict[str(current_Numbers[0])] + ', '
        houseNum = 'д. ' + str(current_Numbers[1]) + ', '
        corp = ""
        if current_Numbers[2]:
            corp = 'корп. ' + str(current_Numbers[2]) + ', '
        fl = 'кв. ' + str(current_Numbers[3])
        yield country + city +  streetName + houseNum + corp + fl


def read_json_from_the_file(fname):
    with open(fname, 'r', encoding='utf8') as f:
        result = json.load(f)
    return result


def validate_streets(in_str):
    if isinstance(in_str, str):
        reg_ex = "(ул. |улица |пр. |проспект )[а-яёА-ЯЁ]*"
        if re.match(reg_ex, in_str, re.IGNORECASE):
            return True
        return False
    return False


def ran_numbers(dict_):
    return [choice(list(dict_.keys())), randint(1,99), randint(0,3), randint(1,144)]

counter = 0
for i in generate_random_add('Россия', 'Новосибирск', 'streets.json'):
    counter += 1
    print(i)
    if counter > 5:
        break

# 2
