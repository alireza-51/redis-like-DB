from typing import List
import asyncio
from asyncio import StreamReader, StreamWriter
from command_registry import COMMANDS
from parsers import parse_request
from exceptions import ClientDisconnected
from log import logger
import settings


async def handle_commands(writer: StreamWriter, message: List[bytes]):
    cmd_name = message[0].upper()
    args = message[1:]

    cmd_class = COMMANDS.get(cmd_name)
    if not cmd_class:
        writer.write(b"-ERR unknown command\r\n")
        await writer.drain()
    else:
        cmd = cmd_class()
        response = cmd.execute(args)
        writer.write(response)
        await writer.drain()

async def handle_client(reader: StreamReader, writer: StreamWriter):
    addr = writer.get_extra_info('peername')
    logger.info(f"Connection from {addr!r}")

    while True:
        try:
            parsed_message = await parse_request(reader)
        except ClientDisconnected:
            break
        if not parsed_message:
            break
        logger.debug(f"Parsed message: {parsed_message}")
        await handle_commands(writer, parsed_message)

    logger.info(f"Close the connection from {addr!r}")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, settings.HOST, settings.PORT)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logger.info(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
