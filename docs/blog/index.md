
# 📖 Developer Blog Index

This blog documents the thought process, architectural decisions, mistakes, and improvements made during the development of this Redis-like server.

---

## ✅ `/docs/blog/index.md`
Blog Index & Module Map

---

## ✅ `commands.py`
Designing a modular command system.  
📄 [commands.md](commands.md)

---

## ✅ `datastore.py`
Implementing a singleton in-memory store.  
📄 [datastore.md](datastore.md)

---

## ✅ `parsers.py`
Parsing raw RESP protocol with flexibility and Open/Closed principle in mind.  
📄 [parsers.md](parsers.md)

---

## ✅ `serializers.py`
RESP-compliant output generation, and why we centralized response formatting.  
📄 [serializers.md](serializers.md)

---

## ✅ `command_registry.py`
Registry for binding command keywords to their handlers.  
📄 [command_registry.md](command_registry.md)

---

## ✅ `server.py`
Building the asyncio-based server loop, and handling edge cases like disconnects.  
📄 [server.md](server.md)

---

## ✅ `exceptions.py`
Defining custom protocol and runtime errors cleanly.  
📄 [exceptions.md](exceptions.md)