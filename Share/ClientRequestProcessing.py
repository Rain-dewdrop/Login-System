from timetips import *
import sys
def ClientRequestProcessing(command):
    # 判断是否是验证登录信息的命令
    if command.startswith("request_verify_login_password_") and "_nameword_" in command:
        print(1)
        return "1"
    # 判断是否是获取服务端IV的命令
    elif command == "request_get_iv":
        print(2)
        return "2"
    # 判断是否是获取服务端key的命令
    elif command == "request_get_key":
        print(3)
        return "3"
    # 判断是否是获取到期时间的命令
    elif command == "request_get_time":
        print(4)
        return "4"
    elif command.startwith("request_verify_Activation_Code_"):
        print(5)
        return "5"
    else:
        timetips("Unknown command.")
        return "Unknown command."
print(sys.path)