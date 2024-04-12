# file tornado/escape.py:242-258
# lines [242, 247, 248, 249, 251, 252, 253, 254, 255, 256, 258]
# branches ['247->248', '247->251', '251->252', '251->253', '253->254', '253->255', '255->256', '255->258']

import pytest
from tornado.escape import recursive_unicode, to_unicode

def test_recursive_unicode():
    # Test with a dictionary containing bytes
    input_dict = {b'key': b'value'}
    expected_dict = {'key': 'value'}
    assert recursive_unicode(input_dict) == expected_dict

    # Test with a list containing bytes
    input_list = [b'item1', b'item2']
    expected_list = ['item1', 'item2']
    assert recursive_unicode(input_list) == expected_list

    # Test with a tuple containing bytes
    input_tuple = (b'item1', b'item2')
    expected_tuple = ('item1', 'item2')
    assert recursive_unicode(input_tuple) == expected_tuple

    # Test with a nested structure
    input_nested = {b'key': [b'item1', (b'item2', {b'key2': b'value2'})]}
    expected_nested = {'key': ['item1', ('item2', {'key2': 'value2'})]}
    assert recursive_unicode(input_nested) == expected_nested

    # Test with non-bytes object
    input_non_bytes = 123
    assert recursive_unicode(input_non_bytes) == input_non_bytes

    # Test with bytes object
    input_bytes = b'some bytes'
    expected_str = to_unicode(input_bytes)
    assert recursive_unicode(input_bytes) == expected_str

@pytest.fixture(autouse=True)
def clean_up():
    # Fixture to clean up state after tests
    yield
    # No cleanup needed for this test function as it does not modify any global state

# No top-level code is needed as per the instructions
