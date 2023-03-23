import asyncio
import aioconsole

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    while True:
        message = await aioconsole.ainput("> ")
        writer.write(message.encode() + b'\n')
        await writer.drain()

        response = await reader.readline()
        response_lines = response.decode().strip().split(',')
        for line in response_lines:
            print(line)

        if message.strip() == 'exit':
            break
        
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
