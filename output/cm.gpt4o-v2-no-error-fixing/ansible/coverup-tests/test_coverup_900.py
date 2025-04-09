# file: lib/ansible/plugins/filter/core.py:202-208
# asked: {"lines": [203, 207, 208], "branches": [[203, 207], [203, 208]]}
# gained: {"lines": [203, 207, 208], "branches": [[203, 207], [203, 208]]}

import pytest
from ansible.plugins.filter.core import from_yaml
from ansible.module_utils.six import string_types

def test_from_yaml_with_string(mocker):
    mock_yaml_load = mocker.patch('ansible.plugins.filter.core.yaml_load', return_value='mocked_yaml')
    mock_to_text = mocker.patch('ansible.plugins.filter.core.to_text', return_value='mocked_text')
    mock_text_type = mocker.patch('ansible.plugins.filter.core.text_type', return_value='mocked_text_type')

    data = "some yaml string"
    result = from_yaml(data)

    mock_to_text.assert_called_once_with(data, errors='surrogate_or_strict')
    mock_text_type.assert_called_once_with('mocked_text')
    mock_yaml_load.assert_called_once_with('mocked_text_type')
    assert result == 'mocked_yaml'

def test_from_yaml_with_non_string():
    data = {"key": "value"}
    result = from_yaml(data)
    assert result == data
