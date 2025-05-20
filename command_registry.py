from typing import Dict, Type
from commands import *


COMMANDS: Dict[bytes, Type[Command]] = {
    b"SET": SetCommand,
    b"GET": GetCommand,
    b'DEL': DelCommand,
}