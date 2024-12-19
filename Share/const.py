import configparser
import threading
import os
usernameHEX = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"  #用户名哈希值
passwordHEX = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"  #密码哈希值
titlesize = f"github.com/Rain-dewdrop/Login-System"  #窗口基础设置
#(测试账户 username:1 password:1)
SERVER_HOST = "127.0.0.1"
Login_status = False
Port_Number = 8888
Max_Bytes = 1024
w = 900
h = 520
key = b'\xb1T\xa3)s\x0ei-\x8c,\x02\xe7\xc3c=\xb0\x98\x86}<\x956\x96\xa0G\xa6-$"#\xdf\x8c'  # 32字节，用于AES-256
iv = b'\xa6\x0eE\x19\xdeu\x10It\x00\x1cb\x95\x88)~' # 16字节，用于AES

current_path = os.path.realpath(__file__)
directory_path = os.path.dirname(current_path)  #当前文件路径
config_file_path = os.path.join(directory_path, 'config.ini')

config = configparser.ConfigParser()

condition = threading.Condition()
