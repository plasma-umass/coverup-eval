# file lib/ansible/module_utils/common/text/converters.py:286-302
# lines [286, 293, 294, 295, 296, 297, 298, 299, 300, 302]
# branches ['293->294', '293->295', '295->296', '295->297', '297->298', '297->299', '299->300', '299->302']

import pytest
from ansible.module_utils.common.text.converters import container_to_bytes
from ansible.module_utils._text import to_bytes, text_type

def test_container_to_bytes():
    # Test with a string
    assert container_to_bytes('test') == to_bytes('test')

    # Test with a dictionary
    input_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_dict = {to_bytes('key1'): to_bytes('value1'), to_bytes('key2'): to_bytes('value2')}
    assert container_to_bytes(input_dict) == expected_dict

    # Test with a list
    input_list = ['value1', 'value2']
    expected_list = [to_bytes('value1'), to_bytes('value2')]
    assert container_to_bytes(input_list) == expected_list

    # Test with a tuple
    input_tuple = ('value1', 'value2')
    expected_tuple = (to_bytes('value1'), to_bytes('value2'))
    assert container_to_bytes(input_tuple) == expected_tuple

    # Test with a mixed container
    input_mixed = {
        'key1': ['value1', 'value2'],
        'key2': ('value3', 'value4'),
        'key3': {'subkey1': 'value5'}
    }
    expected_mixed = {
        to_bytes('key1'): [to_bytes('value1'), to_bytes('value2')],
        to_bytes('key2'): (to_bytes('value3'), to_bytes('value4')),
        to_bytes('key3'): {to_bytes('subkey1'): to_bytes('value5')}
    }
    assert container_to_bytes(input_mixed) == expected_mixed

    # Test with non-container type
    assert container_to_bytes(123) == 123
    assert container_to_bytes(12.34) == 12.34
    assert container_to_bytes(True) == True
