class NotValidRESPMessage(Exception):
    """Raised when the client sends wrong message"""
    pass

class ClientDisconnected(Exception):
    """Raised when the client closes the connection."""
    pass
