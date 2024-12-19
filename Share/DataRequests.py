import asyncio
from const import *
from timetips import *

async def request_data(data_to_send):
    # 连接到服务器
    reader, writer = await asyncio.open_connection(SERVER_HOST, Port_Number)
    timetips(f"向服务端发送数据 {data_to_send}")
    # 发送数据
    writer.write(data_to_send.encode('utf-8'))
    await writer.drain()  # 确保数据发送完成
    
    # 等待服务器的响应
    data_received = await reader.read(Max_Bytes) 
    timetips(f"服务端返回数据: {data_received.decode('utf-8')}")
    saverdata = {data_received.decode('utf-8')}
    
    # 关闭连接
    writer.close()
    await writer.wait_closed()
    return saverdata

# 运行客户端
asyncio.run(request_data('request_verify_login_password_{密码哈希值}_nameword_{用户名哈希值}'))
