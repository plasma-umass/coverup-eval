# file: lib/ansible/module_utils/common/text/converters.py:305-322
# asked: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}
# gained: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_text
from ansible.module_utils.six import binary_type

def test_container_to_text_with_binary_type(mocker):
    mock_to_text = mocker.patch('ansible.module_utils.common.text.converters.to_text', return_value='decoded')
    binary_data = binary_type(b'binary data')
    result = container_to_text(binary_data)
    mock_to_text.assert_called_once_with(binary_data, encoding='utf-8', errors='surrogate_or_strict')
    assert result == 'decoded'

def test_container_to_text_with_dict(mocker):
    mock_to_text = mocker.patch('ansible.module_utils.common.text.converters.to_text', side_effect=lambda obj, encoding, errors: obj.decode(encoding, errors) if isinstance(obj, binary_type) else obj)
    data = {'key': b'value'}
    result = container_to_text(data)
    assert result == {'key': 'value'}

def test_container_to_text_with_list(mocker):
    mock_to_text = mocker.patch('ansible.module_utils.common.text.converters.to_text', side_effect=lambda obj, encoding, errors: obj.decode(encoding, errors) if isinstance(obj, binary_type) else obj)
    data = [b'value1', b'value2']
    result = container_to_text(data)
    assert result == ['value1', 'value2']

def test_container_to_text_with_tuple(mocker):
    mock_to_text = mocker.patch('ansible.module_utils.common.text.converters.to_text', side_effect=lambda obj, encoding, errors: obj.decode(encoding, errors) if isinstance(obj, binary_type) else obj)
    data = (b'value1', b'value2')
    result = container_to_text(data)
    assert result == ('value1', 'value2')

def test_container_to_text_with_other_type(mocker):
    mock_to_text = mocker.patch('ansible.module_utils.common.text.converters.to_text', side_effect=lambda obj, encoding, errors: obj.decode(encoding, errors) if isinstance(obj, binary_type) else obj)
    data = 12345
    result = container_to_text(data)
    assert result == 12345
