import definition as t

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
    else:
        t.timetips("Unknown command.")
        return "Unknown command."