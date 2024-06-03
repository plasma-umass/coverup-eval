# file lib/ansible/plugins/filter/core.py:202-208
# lines [202, 203, 207, 208]
# branches ['203->207', '203->208']

import pytest
from ansible.plugins.filter.core import from_yaml
from ansible.module_utils._text import to_text
import yaml

def test_from_yaml_string(mocker):
    mocker.patch('ansible.plugins.filter.core.yaml_load', return_value={'key': 'value'})
    data = 'key: value'
    result = from_yaml(data)
    assert result == {'key': 'value'}

def test_from_yaml_non_string():
    data = {'key': 'value'}
    result = from_yaml(data)
    assert result == data
