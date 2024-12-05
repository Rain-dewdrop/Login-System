import asyncio as a
import const
import definition as t
import ClientRequestProcessing as c

async def handle_client(reader,writer):
    data = await reader.read(const.Max_Bytes)
    t.timetips(f"接收到客户端数据：{data}")
    response = bytes(c.ClientRequestProcessing(data))
    writer.write(response)
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