# file: lib/ansible/module_utils/common/text/converters.py:305-322
# asked: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}
# gained: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_text
from ansible.module_utils._text import to_text, binary_type

def test_container_to_text_with_binary_type():
    binary_data = b'binary data'
    result = container_to_text(binary_data)
    assert result == to_text(binary_data)

def test_container_to_text_with_dict(monkeypatch):
    test_dict = {b'key1': b'value1', b'key2': b'value2'}
    
    def mock_to_text(data, encoding='utf-8', errors='surrogate_or_strict'):
        return data.decode(encoding, errors)
    
    monkeypatch.setattr('ansible.module_utils._text.to_text', mock_to_text)
    
    result = container_to_text(test_dict)
    expected = {mock_to_text(k): mock_to_text(v) for k, v in test_dict.items()}
    assert result == expected

def test_container_to_text_with_list(monkeypatch):
    test_list = [b'value1', b'value2']
    
    def mock_to_text(data, encoding='utf-8', errors='surrogate_or_strict'):
        return data.decode(encoding, errors)
    
    monkeypatch.setattr('ansible.module_utils._text.to_text', mock_to_text)
    
    result = container_to_text(test_list)
    expected = [mock_to_text(v) for v in test_list]
    assert result == expected

def test_container_to_text_with_tuple(monkeypatch):
    test_tuple = (b'value1', b'value2')
    
    def mock_to_text(data, encoding='utf-8', errors='surrogate_or_strict'):
        return data.decode(encoding, errors)
    
    monkeypatch.setattr('ansible.module_utils._text.to_text', mock_to_text)
    
    result = container_to_text(test_tuple)
    expected = tuple(mock_to_text(v) for v in test_tuple)
    assert result == expected

def test_container_to_text_with_other_type():
    test_value = 12345
    result = container_to_text(test_value)
    assert result == test_value
