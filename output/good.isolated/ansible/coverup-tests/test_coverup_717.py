# file lib/ansible/cli/doc.py:515-517
# lines [515, 516, 517]
# branches []

import pytest
import pkgutil
from ansible.cli.doc import DocCLI
from unittest.mock import patch, MagicMock

# Assuming the existence of a file 'keyword_desc.yml' in the 'ansible' package directory
# If the file does not exist, the test should be adjusted accordingly.

@pytest.fixture
def mock_pkgutil_get_data():
    with patch('pkgutil.get_data', return_value=b'keyword1: description1\nkeyword2: description2') as mock:
        yield mock

def test_list_keywords(mock_pkgutil_get_data):
    # Call the static method to trigger the code under test
    keywords = DocCLI._list_keywords()

    # Verify that pkgutil.get_data was called with the correct arguments
    mock_pkgutil_get_data.assert_called_once_with('ansible', 'keyword_desc.yml')

    # Verify that the returned keywords are as expected
    expected_keywords = {'keyword1': 'description1', 'keyword2': 'description2'}
    assert keywords == expected_keywords, "The keywords returned by _list_keywords do not match the expected values"
