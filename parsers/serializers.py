class RESPSerializer:

    @staticmethod
    def encode_simple_string(s: str) -> bytes:
        return f"+{s}\r\n".encode()

    @staticmethod
    def encode_error(msg: str) -> bytes:
        return f"-ERR {msg}\r\n".encode()

    @staticmethod
    def encode_bulk_string(s: str | None) -> bytes:
        if s is None:
            return b"$-1\r\n"
        return f"${len(s)}\r\n{s}\r\n".encode()

    @staticmethod
    def encode_integer(n: int) -> bytes:
        return f":{n}\r\n".encode()

    @staticmethod
    def encode_array(items: list[bytes]) -> bytes:
        out = [f"*{len(items)}\r\n".encode()]
        out.extend(items)
        return b"".join(out)
