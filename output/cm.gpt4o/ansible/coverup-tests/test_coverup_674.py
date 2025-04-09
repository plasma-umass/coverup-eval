# file lib/ansible/cli/doc.py:515-517
# lines [515, 516, 517]
# branches []

import pytest
from unittest.mock import patch, mock_open
import pkgutil
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pkgutil_get_data(mocker):
    mock_data = "key: value"
    mocker.patch('pkgutil.get_data', return_value=mock_data.encode('utf-8'))
    return mock_data

def test_list_keywords(mock_pkgutil_get_data):
    result = DocCLI._list_keywords()
    assert result == {'key': 'value'}
