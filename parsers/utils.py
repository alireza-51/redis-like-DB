from typing import List
import asyncio

from exceptions import NotValidRESPMessage, ClientDisconnected

async def parse_bulk_string(reader: asyncio.StreamReader) -> bytes | None: 
    length_line = await reader.readline()
    if not length_line.endswith(b'\r\n'):
        raise NotValidRESPMessage("Bulk string length must end with CRLF")
    
    try:
        length = int(length_line[:-2])
    except ValueError:
        raise NotValidRESPMessage(f"Invalid bulk string length: {length_line}")
    
    if length == -1:
        return None
    
    value = await reader.readexactly(length)
    
    crlf = await reader.readexactly(2)
    if crlf != b'\r\n':
        raise NotValidRESPMessage("Bulk string missing CRLF after data")

    return value

async def parse_array(reader: asyncio.StreamReader) -> List[bytes] | None:
    length_line = await reader.readline()
    if not length_line.endswith(b'\r\n'):
        raise NotValidRESPMessage("List length missing CRLF after data")

    try:
        length = int(length_line[:-2])
    except ValueError:
        raise NotValidRESPMessage(f"Invalid list length: {length_line}")
    
    if length == -1:
        return None
    output = []
    for _ in range(length):
        prefix = await reader.readexactly(1)
        parser = PARSERS[prefix]
        if parser is None:
            raise NotValidRESPMessage('Unknown type prefix: {prefix}')
        value = await parser(reader)
        output.append(value)

    return output

async def parse_simple_string(reader: asyncio.StreamReader) -> bytes:
    line = await reader.readline()
    if not line.endswith(b'\r\n'):
        raise NotValidRESPMessage("Simple string must end with CRLF")
    return line[:-2]

async def parse_integer(reader: asyncio.StreamReader) -> int:
    line = await reader.readline()
    if not line.endswith(b'\r\n'):
        raise NotValidRESPMessage("Integer must end with CRLF")
    try:
        return int(line[:-2])
    except ValueError:
        raise NotValidRESPMessage(f"Invalid integer: {line}")

async def parse_error(reader): ...

PARSERS = {
    b'*': parse_array,
    b'$': parse_bulk_string,
    b'+': parse_simple_string,
    b':': parse_integer,
    b'-': parse_error,
}

async def parse_request(reader: asyncio.StreamReader) -> List[bytes]:
    try:
        prefix = await reader.readexactly(1)
    except asyncio.exceptions.IncompleteReadError:
        raise ClientDisconnected()

    if prefix not in PARSERS:
        raise NotValidRESPMessage(f"Unknown RESP prefix: {prefix}")
    return await PARSERS[prefix](reader)
