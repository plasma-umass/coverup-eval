# file: typesystem/base.py:184-185
# asked: {"lines": [185], "branches": []}
# gained: {"lines": [185], "branches": []}

import pytest
from typesystem.base import BaseError

class TestBaseError:
    def test_getitem(self, monkeypatch):
        class MockBaseError(BaseError):
            def __init__(self):
                self._message_dict = {'key1': 'value1', 'key2': 'value2'}
        
        error = MockBaseError()
        
        assert error['key1'] == 'value1'
        assert error['key2'] == 'value2'
        
    def test_getitem_key_error(self, monkeypatch):
        class MockBaseError(BaseError):
            def __init__(self):
                self._message_dict = {'key1': 'value1'}
        
        error = MockBaseError()
        
        with pytest.raises(KeyError):
            _ = error['key3']
