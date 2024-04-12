# file lib/ansible/plugins/filter/core.py:202-208
# lines [203, 207, 208]
# branches ['203->207', '203->208']

import pytest
from ansible.plugins.filter.core import from_yaml
from ansible.module_utils._text import to_bytes

@pytest.fixture
def clean_yaml_loader(mocker):
    # Mock the yaml loader to ensure it does not affect other tests
    mocker.patch('ansible.plugins.filter.core.yaml_load', return_value='mocked_yaml_load')

def test_from_yaml_with_string(clean_yaml_loader):
    test_string = 'key: value'
    # Convert to bytes and back to string to ensure it's a plain string type
    test_string_bytes = to_bytes(test_string)
    test_string_str = test_string_bytes.decode('utf-8')
    result = from_yaml(test_string_str)
    assert result == 'mocked_yaml_load', "The result should be the output of the mocked yaml_load function"

def test_from_yaml_with_non_string(clean_yaml_loader):
    test_dict = {'key': 'value'}
    result = from_yaml(test_dict)
    assert result == test_dict, "The result should be the original data if it's not a string"
