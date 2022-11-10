import asyncio
from asyncio import StreamReader, StreamWriter


async def handler_stream(reader:StreamReader, writer: StreamWriter):
    data = await reader.read(10000)
    print(data.decode())
    http_text = "HTTP/1.1 200 Ok\r\ncontent-type: text/html\r\nserver: zpymserver\r\n\r\n<html><h1>welcome to sii</h1></html>"  #http响应
    writer.write(http_text.encode())
    await writer.drain()    #强制刷新

    print("Close the connection")
    writer.close()



async def server():
    s = await asyncio.start_server(client_connected_cb=handler_stream,host='127.0.0.1',port=8888)
    async with s:
        await s.serve_forever()


if __name__== '__main__':
    asyncio.run(server())