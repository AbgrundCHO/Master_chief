"""
该文件用于加密 Neo4j 数据库的用户名和密码，
新用户在此处执行后即可连接至数据库。
"""

from login import create_keys, encode_message
import os

USERNAME = 'neo4j'
PASSWORD = 'passwords'
key_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'profilekeys', 'password.pem'))


if __name__ == '__main__':
    create_keys()
    with open(key_path, 'w') as f:
        f.write('')
    with open(key_path, 'w+') as f:
        f.write(str(encode_message(USERNAME)))
        f.write('\n')
        f.write(str(encode_message(PASSWORD)))