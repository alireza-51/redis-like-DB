from typing import Dict, Type
from commands import SetCommand, GetCommand, Command


COMMANDS: Dict[bytes, Type[Command]] = {
    b"SET": SetCommand,
    b"GET": GetCommand,
}