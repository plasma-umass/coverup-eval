# file lib/ansible/plugins/filter/core.py:47-54
# lines [54]
# branches []

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.plugins.filter.core import to_yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

def test_to_yaml_success(mocker):
    # Mock yaml.dump to return a specific string
    expected_yaml = 'test: yaml'
    mocker.patch('yaml.dump', return_value=expected_yaml)
    # Ensure to_text is called with the result of yaml.dump
    mock_to_text = mocker.patch('ansible.plugins.filter.core.to_text', side_effect=lambda x: x)

    # Call to_yaml and check if the result is as expected
    result = to_yaml({'test': 'yaml'})
    assert result == expected_yaml
    # Verify that to_text was called with the output of yaml.dump
    mock_to_text.assert_called_once_with(expected_yaml)

    # Clean up mocks
    mocker.stopall()
