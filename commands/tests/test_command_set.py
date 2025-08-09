import pytest
from commands.tests.mocks import mock_datastore
from commands.command_set import (
    GetCommand,
    SetCommand,
    DelCommand,
    IncrCommand,
    IncrByCommand,
)


def test_get_command():
    command = SetCommand()
    res = command.execute([b'get_key', b'value'])
    assert res == b'+OK\r\n'
    
    command = GetCommand()
    res = command.execute([b'get_key'])
    assert res == b'$5\r\nvalue\r\n'


def test_set_command():
    command = SetCommand()
    res = command.execute([b'set_key', b'value'])
    assert res == b'+OK\r\n'
    assert command._data_store.get('set_key') == 'value'

def test_del_command():
    set_command = SetCommand()
    res = set_command.execute([b'key', b'value'])
    assert res == b'+OK\r\n'
    assert set_command._data_store.get('key') == 'value'
    
    del_command = DelCommand()
    res = del_command.execute([b'key'])
    assert res == b'+OK\r\n'
    assert set_command._data_store.get('key') == None

def test_incr_command():
    incr_command = IncrCommand()
    
    # Case of key not in database
    res = incr_command.execute([b'incr_key'])
    assert res == b':1\r\n'
    
    # Case  of key exists in database
    res = incr_command.execute([b'incr_key'])
    assert res == b':2\r\n'
    
    del_command = DelCommand()
    res = del_command.execute([b'incr_key'])
    assert res == b'+OK\r\n'
    

def test_incr_by_command():
    incrby_command = IncrByCommand()
    
    # Case of key not in database
    res = incrby_command.execute([b'incrby_key', b'2'])
    assert res == b':2\r\n'
    
    # Case  of key exists in database
    res = incrby_command.execute([b'incrby_key', b'3'])
    assert res == b':5\r\n'
    
    del_command = DelCommand()
    res = del_command.execute([b'incrby_key'])
    assert res == b'+OK\r\n'
