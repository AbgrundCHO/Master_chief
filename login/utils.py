import codecs
from login import decode_message
import os


key_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'profilekeys', 'password.pem'))


def read_ras_password():
    with open(key_path, 'r') as f:
        username = f.readline().strip()
        password = f.readline().strip()

    return username, password

def decode2str(str_info):
    str_info = bytes(str_info[2:-1], encoding='utf8')
    str_info = codecs.escape_decode(str_info, 'hex-escape')[0]
    str_info = decode_message(str_info)

    return str_info