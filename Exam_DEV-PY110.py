from random import randint
from random import choice
import json
import re
import requests


# 1
def generate_random_add(country_, city_, fname):
    """
    :param country_: Country name
    :param city_: city name
    :param fname: path to json file
    :return: generator of the random addresses
    """
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
        yield normalize_address(country + city +  streetName + houseNum + corp + fl)


def normalize_address(in_str):
    url = "https://otpravka-api.pochta.ru/1.0/clean/address"
    token = "Test_token"
    key = "Test_key"
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json;charset=UTF-8",
        "Authorization": "AccessToken " + token,
        "X-User-Authorization": "Basic " + key
    }
    addresses = [
        {
            "id": "0",
            "original-address": in_str
        }
    ]
    response = requests.post(url, headers=request_headers, data=json.dumps(addresses))
    return response.text


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
def dec_(func):
    def wrapper(*args, is_test='', test=False, **kwargs):
        if is_test.lower() != 'test' and not test:
            result = func(*args, **kwargs)
            return result
        else:
            return f"Вызов функции {func.__name__} с параметрами {args}"
    return wrapper


@dec_
def pow_n(n, pov_):
    """
    :param n: number
    :param pov_: power
    :return: powered number. type is_test = 'test' or test = True to show parameters.
    """
    return n ** pov_
print(pow_n(4, 3, is_test='test'))
print(pow_n(4, 3, test=True))
print(pow_n(4, 3))
