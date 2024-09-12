# file: typesystem/base.py:184-185
# asked: {"lines": [184, 185], "branches": []}
# gained: {"lines": [184, 185], "branches": []}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_getitem():
    messages = [
        Message(text='value1', code='code1', key='key1'),
        Message(text='value2', code='code2', key='key2')
    ]
    error = BaseError(messages=messages)
    
    assert error['key1'] == 'value1'
    assert error['key2'] == 'value2'
    
    with pytest.raises(KeyError):
        _ = error['key3']
