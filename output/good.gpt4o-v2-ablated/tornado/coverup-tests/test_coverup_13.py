# file: tornado/escape.py:242-258
# asked: {"lines": [242, 247, 248, 249, 251, 252, 253, 254, 255, 256, 258], "branches": [[247, 248], [247, 251], [251, 252], [251, 253], [253, 254], [253, 255], [255, 256], [255, 258]]}
# gained: {"lines": [242, 247, 248, 249, 251, 252, 253, 254, 255, 256, 258], "branches": [[247, 248], [247, 251], [251, 252], [251, 253], [253, 254], [253, 255], [255, 256], [255, 258]]}

import pytest
from tornado.escape import to_unicode
from tornado.escape import recursive_unicode

def test_recursive_unicode_dict():
    input_data = {b'key1': b'value1', b'key2': {b'key3': b'value3'}}
    expected_output = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    assert recursive_unicode(input_data) == expected_output

def test_recursive_unicode_list():
    input_data = [b'value1', [b'value2', b'value3']]
    expected_output = ['value1', ['value2', 'value3']]
    assert recursive_unicode(input_data) == expected_output

def test_recursive_unicode_tuple():
    input_data = (b'value1', (b'value2', b'value3'))
    expected_output = ('value1', ('value2', 'value3'))
    assert recursive_unicode(input_data) == expected_output

def test_recursive_unicode_bytes():
    input_data = b'value1'
    expected_output = 'value1'
    assert recursive_unicode(input_data) == expected_output

def test_recursive_unicode_other():
    input_data = 12345
    expected_output = 12345
    assert recursive_unicode(input_data) == expected_output
