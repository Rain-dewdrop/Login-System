import arrow
import tkinter.messagebox as messagebox
import hashlib
import configparser
import wmi
import base64
import threading
from plyer import notification
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# 硬编码的密钥和IV
key = b'\xb1T\xa3)s\x0ei-\x8c,\x02\xe7\xc3c=\xb0\x98\x86}<\x956\x96\xa0G\xa6-$"#\xdf\x8c'  # 32字节，用于AES-256
iv = b'\xa6\x0eE\x19\xdeu\x10It\x00\x1cb\x95\x88)~' # 16字节，用于AES

current_path = os.path.realpath(__file__)
directory_path = os.path.dirname(current_path)  #当前文件路径
config_file_path = os.path.join(directory_path, 'config.ini')

config = configparser.ConfigParser()

condition = threading.Condition()

def timetips(message):

    print(f"[{arrow.now().format('HH:mm:ss')}] {message}")

    return

def message(message):
    timetips(f"已弹窗提醒 内容:{message}")

    messagebox.askyesno(message=message,title="github.com/Rain-dewdrop")

    return

def HEX(t):
    if t == "":
        sha256_hash = hashlib.sha256()
        timetips("创建 SHA-256 对象成功！")

        timetips("哈希值计算失败 : 内容空")

    else:
        sha256_hash = hashlib.sha256()
        timetips("创建 SHA-256 对象成功！")

        data = t.encode()
        sha256_hash.update(data)
        hex_digest = sha256_hash.hexdigest()
        timetips("哈希值计算成功！")

        return hex_digest
    
    return

def cfgget(select,message):

    return config.get(select,message)

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

def get_hwid():
     # 创建 WMI 客户端
    c = wmi.WMI()
    # 查询主板信息
    for board in c.Win32_BaseBoard():
        # 返回主板的序列号

        return board.SerialNumber
    return

def send_notification(__title5__, __message5__):
    timetips(f"已发送消息 内容:{__message5__}")
    notification.notify(
        title=__title5__,
        message=__message5__,
        app_icon=None,
        timeout=2,
    )
    return
