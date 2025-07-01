from typing import Dict, Type


COMMANDS: Dict[bytes, Type["Command"]] = {}

def register(command: bytes | None = None):
    def decorator(cls):
        key = command or cls.__name__.upper().encode()            
        if key in COMMANDS:
            raise ValueError('Command is already registered')
        
        COMMANDS[key] = cls
        
        return cls
    return decorator

def init_commands():
    import commands # noqa: F401
