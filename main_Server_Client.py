import asyncio as a
import const
import definition as t
import ClientRequestProcessing as c


async def handle_client(reader, writer):
    data = await reader.read(const.Max_Bytes)
    t.timetips(f"接收到客户端数据：{data}")
    
    # 将字节数据解码为字符串，然后处理请求
    command = data.decode('utf-8')
    response = c.ClientRequestProcessing(command)
    
    # 将处理结果编码为字节，然后发送给客户端
    writer.write(response.encode('utf-8'))
    t.timetips(f"向客户端发送数据：{response}")
    
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    return

async def main():
    sever = await a.start_server(handle_client,const.SERVER_HOST,const.Port_Number)
    t.timetips(f"服务器已开启在 端口：{const.Port_Number}")
    async with sever:
        await sever.serve_forever()
    return



a.run(main())



"""
import os
key = os.urandom(32)
iv = os.urandom(16)
print(iv,iv)
print(key,key)
"""