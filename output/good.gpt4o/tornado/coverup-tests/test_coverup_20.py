# file tornado/escape.py:242-258
# lines [242, 247, 248, 249, 251, 252, 253, 254, 255, 256, 258]
# branches ['247->248', '247->251', '251->252', '251->253', '253->254', '253->255', '255->256', '255->258']

import pytest
from tornado.escape import to_unicode

def test_recursive_unicode():
    from tornado.escape import recursive_unicode

    # Test with a dictionary containing bytes
    input_dict = {b'key1': b'value1', b'key2': {b'key3': b'value3'}}
    expected_dict = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    assert recursive_unicode(input_dict) == expected_dict

    # Test with a list containing bytes
    input_list = [b'value1', [b'value2', b'value3']]
    expected_list = ['value1', ['value2', 'value3']]
    assert recursive_unicode(input_list) == expected_list

    # Test with a tuple containing bytes
    input_tuple = (b'value1', (b'value2', b'value3'))
    expected_tuple = ('value1', ('value2', 'value3'))
    assert recursive_unicode(input_tuple) == expected_tuple

    # Test with a mixed structure
    input_mixed = {b'key1': [b'value1', (b'value2', {b'key2': b'value3'})]}
    expected_mixed = {'key1': ['value1', ('value2', {'key2': 'value3'})]}
    assert recursive_unicode(input_mixed) == expected_mixed

    # Test with a non-bytes object
    input_non_bytes = 'string'
    assert recursive_unicode(input_non_bytes) == 'string'

    # Test with bytes
    input_bytes = b'bytes'
    assert recursive_unicode(input_bytes) == to_unicode(input_bytes)
