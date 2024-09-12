# file: lib/ansible/cli/doc.py:515-517
# asked: {"lines": [515, 516, 517], "branches": []}
# gained: {"lines": [515, 516, 517], "branches": []}

import pytest
import pkgutil
from unittest.mock import patch, mock_open
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pkgutil_get_data():
    with patch('pkgutil.get_data') as mock_get_data:
        yield mock_get_data

def test_list_keywords(mock_pkgutil_get_data):
    mock_yaml_content = "key: value"
    mock_pkgutil_get_data.return_value = mock_yaml_content

    result = DocCLI._list_keywords()

    mock_pkgutil_get_data.assert_called_once_with('ansible', 'keyword_desc.yml')
    assert result == {'key': 'value'}
