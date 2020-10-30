import rsa
import os

key_dir = os.path.join(os.path.dirname(__file__), 'profilekeys')
public_key = os.path.abspath(os.path.join(key_dir, 'public.pem'))
private_key = os.path.abspath(os.path.join(key_dir, 'private.pem'))

def create_keys(length=1024):
    # 生成密钥：生成RSA公钥和秘钥
    (pubkey, privkey) = rsa.newkeys(length)

    # 保存密钥(一个公钥一个私钥)
    with open(public_key, 'w+') as f:
        f.write(pubkey.save_pkcs1().decode())
    with open(private_key, 'w+') as f:
        f.write(privkey.save_pkcs1().decode())

def get_pubkey():
    with open(public_key, 'r') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

    return pubkey

def get_privkey():
    with open(private_key, 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

    return privkey

def encode_message(message):
    # 公钥对明文加密，得到密文
    pubkey = get_pubkey()
    crypto = rsa.encrypt(message.encode(), pubkey)

    return crypto

def decode_message(crypto):
    # 私钥对密文解密，得到明文
    privkey = get_privkey()
    message = rsa.decrypt(crypto, privkey).decode()

    return message

def encode_sign(message):
    # 私钥签名
    privkey = get_privkey()
    signature = rsa.sign(message.encode("utf-8"), privkey, 'SHA-1')

    return signature

def verify_sign(message, signature):
    # 公钥验证：同时收到指令明文、密文，然后用公钥验证，进行身份确认
    pubkey = get_pubkey()
    result = True

    try:
        rsa.verify(message.encode("utf-8"), signature, pubkey)
    except rsa.pkcs1.VerificationError:
        result = False
    finally:
        return result
