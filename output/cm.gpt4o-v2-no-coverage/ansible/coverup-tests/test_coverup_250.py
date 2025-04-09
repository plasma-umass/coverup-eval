# file: lib/ansible/module_utils/common/text/converters.py:286-302
# asked: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}
# gained: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_bytes
from ansible.module_utils.six import text_type

def test_container_to_bytes_with_string(mocker):
    mock_to_bytes = mocker.patch('ansible.module_utils.common.text.converters.to_bytes', return_value=b'test')
    result = container_to_bytes('test')
    mock_to_bytes.assert_called_once_with('test', encoding='utf-8', errors='surrogate_or_strict')
    assert result == b'test'

def test_container_to_bytes_with_dict(mocker):
    mock_to_bytes = mocker.patch('ansible.module_utils.common.text.converters.to_bytes', side_effect=lambda x, encoding, errors: x.encode(encoding, errors))
    input_dict = {'key': 'value'}
    result = container_to_bytes(input_dict)
    assert result == {b'key': b'value'}

def test_container_to_bytes_with_list(mocker):
    mock_to_bytes = mocker.patch('ansible.module_utils.common.text.converters.to_bytes', side_effect=lambda x, encoding, errors: x.encode(encoding, errors))
    input_list = ['value1', 'value2']
    result = container_to_bytes(input_list)
    assert result == [b'value1', b'value2']

def test_container_to_bytes_with_tuple(mocker):
    mock_to_bytes = mocker.patch('ansible.module_utils.common.text.converters.to_bytes', side_effect=lambda x, encoding, errors: x.encode(encoding, errors))
    input_tuple = ('value1', 'value2')
    result = container_to_bytes(input_tuple)
    assert result == (b'value1', b'value2')

def test_container_to_bytes_with_non_container():
    input_value = 12345
    result = container_to_bytes(input_value)
    assert result == 12345
