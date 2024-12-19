import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from const import *
def b64(enc_data):
# Base64解码
    decoded = base64.b64decode(enc_data)
    # 提取IV和加密数据
    iv = decoded[:AES.block_size]
    encrypted = decoded[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密数据
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    
    return decrypted.decode('utf-8')

def b64code(data):
# 加密数据
    global iv,key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    # Base64编码加密后的数据

    return base64.b64encode(iv + encrypted).decode('utf-8')