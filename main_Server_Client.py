# import os
# # 生成一个随机密钥（例如，用于AES-256）
# key = os.urandom(32)  # AES-256需要一个256位的密钥
# # 生成一个随机IV（初始化向量），对于AES，通常是128位
# iv = os.urandom(16)  # AES需要一个128位的IV
# print(iv)
# print(key)
import asyncio as a
import const
import definition as t

async def handle_client(reader,writer):
    data = await reader.read(const.Max_Bytes)
    t.timetips(data)

    response = b'Hello, client!'
    writer.write(response)
    await writer.drain()  # 确保数据发送完成

    # 关闭连接
    writer.close()
    await writer.wait_closed()
    return

async def main():
    sever = await a.start_server(handle_client,const.SERVER_HOST,const.Port_Number)
    print(f"服务器已开启在 端口：{const.Port_Number}")
    async with sever:
        await sever.serve_forever()
    return

a.run(main())