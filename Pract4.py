import re

#IP4 regex
print(re.match(r"^((([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))$"))

nat_num = r"^[1-9]$|([0-9]{2,})$"
abb = r"\s[A-ZА-ЯЁ]{1,}\s"
empty_string = r"^\s*$"
rand_text = r"[A-ZА-Я]([а-яa-z0-9]*\s*)*\."
e_mail = r"([a-zA-Z0-9]){1,}\@([a-zA-Z0-9]){1,}\.(ru|com)"
url_get = r'http(s)*:\\\\[a-zA-Z]{1,}.(ru|com)(\\[0-9a-zA-Z]*)*\?([0-9a-zA-Z]*)\=([0-9a-zA-Z]*)'

# 2
def check_is_ISO(str_date):
    reg_ex = r"^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$"
    does_match = re.compile(reg_ex).match
    if does_match(str_date):
        return True
    else:
        return False

print(check_is_ISO('2020-12-05'))
print(check_is_ISO('2020-30-30'))
