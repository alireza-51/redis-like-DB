from typing import Any, List
from datastore import DataStore
from serializers import RESPSerializer as RESP


class Command:
    _data_store = DataStore()

    def execute(self, args: List[bytes]) -> bytes:
        raise NotImplementedError
    

class SetCommand(Command):
    def execute(self, args: List[bytes]) -> bytes:
        if len(args) != 2:
            return RESP.encode_error("wrong number of arguments for 'SET'")
        key = args[0].decode()
        value = args[1].decode()
        self._data_store.set(key=key, value=value)
        return RESP.encode_simple_string("+SET")


class GetCommand(Command):
    def execute(self, args:List[bytes]) -> bytes:
        if len(args) != 1:
            return RESP.encode_error("wrong number of arguments for 'GET'")
        key = args[0].decode()
        data = self._data_store.get(key=key)
        
        if data is None:
            return RESP.encode_bulk_string(None)

        return RESP.encode_bulk_string(data)

class DelCommand(Command):
    def execute(self, args:List[bytes]) -> bytes:
        
        if len(args) != 1:
            return RESP.encode_error("wrong number of arguments for 'DEL'")
        
        key = args[0].decode()
        try:
            self._data_store.delete(key=key)
            return RESP.encode_simple_string('+DEL')
        except KeyError:
            return RESP.encode_error(f"'{key}' key not found.")
