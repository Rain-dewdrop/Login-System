"""
请求命令:
[request_verify_login_password_{密码哈希值}_nameword_{用户名哈希值}] 验证登录信息
[request_get_iv] 获取服务端iv
[request_get_key] 获取服务端key
"""
import definition as t
import asyncio as a

async def ClientRequestProcessing(command_bytes):
    # 将字节类型转换为字符串类型
    command = command_bytes.decode('utf-8')
    
    # 判断是否是验证登录信息的命令
    if command.startswith("request_verify_login_password_") and "_nameword_" in command:
        print(1)
        return 1
    # 判断是否是获取服务端IV的命令
    elif command == "request_get_iv":
        print(2)
        return 2
    # 判断是否是获取服务端key的命令
    elif command == "request_get_key":
        print(3)
        return 3
    else:
        t.timetips("Unknown command.")
        return "Unknown command."