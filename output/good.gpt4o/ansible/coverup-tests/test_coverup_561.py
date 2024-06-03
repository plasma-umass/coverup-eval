# file lib/ansible/plugins/filter/core.py:211-217
# lines [211, 212, 216, 217]
# branches ['212->216', '212->217']

import pytest
from ansible.plugins.filter.core import from_yaml_all
from ansible.module_utils.six import string_types
import yaml

def test_from_yaml_all_string(mocker):
    mocker.patch('ansible.plugins.filter.core.to_text', return_value='- item1\n- item2')
    mocker.patch('ansible.plugins.filter.core.yaml_load_all', return_value=['item1', 'item2'])

    data = '- item1\n- item2'
    result = from_yaml_all(data)
    
    assert result == ['item1', 'item2']

def test_from_yaml_all_non_string():
    data = ['item1', 'item2']
    result = from_yaml_all(data)
    
    assert result == data
