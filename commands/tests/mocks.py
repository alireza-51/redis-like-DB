from unittest.mock import Mock
import pytest

DATA_STORE = dict()

@pytest.fixture
def mock_datastore(mocker):
    data_store_mock = Mock()
    data_store_mock.get = DATA_STORE.get()
    data_store_mock.set = DATA_STORE.__setattr__()
    data_store_mock.delete = DATA_STORE.pop()
    return data_store_mock
