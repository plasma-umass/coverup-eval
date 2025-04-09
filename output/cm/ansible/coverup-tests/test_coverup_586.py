# file lib/ansible/plugins/filter/core.py:211-217
# lines [211, 212, 216, 217]
# branches ['212->216', '212->217']

import pytest
from ansible.plugins.filter.core import from_yaml_all
from ansible.module_utils._text import to_text
from yaml import load_all as yaml_load_all, CSafeLoader

# Mocking string_types to simulate the expected behavior
string_types = (str,)

# Mocking the yaml_load_all function to return a controlled output
@pytest.fixture
def mock_yaml_load_all(mocker):
    return mocker.patch('ansible.plugins.filter.core.yaml_load_all', return_value=['a', 'b', 'c'])

# Test function to cover from_yaml_all with string input
def test_from_yaml_all_with_string_input(mock_yaml_load_all):
    test_data = "test string"
    result = from_yaml_all(test_data)
    assert result == ['a', 'b', 'c']
    mock_yaml_load_all.assert_called_once_with(to_text(test_data, errors='surrogate_or_strict'))

# Test function to cover from_yaml_all with non-string input
def test_from_yaml_all_with_non_string_input():
    test_data = ['already', 'a', 'list']
    result = from_yaml_all(test_data)
    assert result == test_data
