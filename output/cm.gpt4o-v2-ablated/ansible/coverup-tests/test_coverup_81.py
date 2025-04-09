# file: lib/ansible/module_utils/common/text/converters.py:305-322
# asked: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}
# gained: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_text
from ansible.module_utils._text import to_text, binary_type
from ansible.module_utils.six import iteritems

def test_container_to_text_binary_type(monkeypatch):
    binary_data = b'binary data'
    expected_text = to_text(binary_data, encoding='utf-8', errors='surrogate_or_strict')
    
    result = container_to_text(binary_data)
    
    assert result == expected_text

def test_container_to_text_dict(monkeypatch):
    data = {b'key1': b'value1', b'key2': b'value2'}
    expected = {'key1': 'value1', 'key2': 'value2'}
    
    result = container_to_text(data)
    
    assert result == expected

def test_container_to_text_list(monkeypatch):
    data = [b'value1', b'value2']
    expected = ['value1', 'value2']
    
    result = container_to_text(data)
    
    assert result == expected

def test_container_to_text_tuple(monkeypatch):
    data = (b'value1', b'value2')
    expected = ('value1', 'value2')
    
    result = container_to_text(data)
    
    assert result == expected

def test_container_to_text_mixed(monkeypatch):
    data = {
        b'key1': [b'value1', b'value2'],
        b'key2': (b'value3', b'value4'),
        b'key3': {b'key4': b'value5'}
    }
    expected = {
        'key1': ['value1', 'value2'],
        'key2': ('value3', 'value4'),
        'key3': {'key4': 'value5'}
    }
    
    result = container_to_text(data)
    
    assert result == expected

def test_container_to_text_non_container(monkeypatch):
    data = 12345
    
    result = container_to_text(data)
    
    assert result == data
