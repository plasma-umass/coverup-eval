# file typesystem/base.py:184-185
# lines [184, 185]
# branches []

import pytest
from typesystem.base import BaseError

def test_base_error_getitem():
    error = BaseError(text='Error occurred')
    error._message_dict = {'key1': 'value1', 'key2': {'nested_key': 'nested_value'}}

    # Test __getitem__ for a top-level key
    assert error['key1'] == 'value1'

    # Test __getitem__ for a nested key
    assert error['key2'] == {'nested_key': 'nested_value'}

    # Test __getitem__ for a non-existent key, should raise KeyError
    with pytest.raises(KeyError):
        error['non_existent_key']
