# file lib/ansible/cli/doc.py:985-995
# lines [990, 991, 992, 993, 994, 995]
# branches ['991->992', '991->995', '993->991', '993->994']

import os
import pytest
from ansible.cli.doc import DocCLI
from unittest.mock import MagicMock

# Mock the Display class to avoid any actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display')

# Create a fixture for the finder with a custom _get_paths method
@pytest.fixture
def mock_finder(mocker):
    finder = MagicMock()
    finder._get_paths = MagicMock(return_value=['/path/to/plugins', '/path/to/plugins'])
    return finder

# Test function to cover lines 990-995
def test_print_paths(mock_display, mock_finder):
    # Call the static method with the mocked finder
    paths = DocCLI.print_paths(mock_finder)
    
    # Assertions to verify the postconditions
    assert paths == '/path/to/plugins', "The paths should be deduplicated and joined by os.pathsep"
    # Ensure that _get_paths was called with the correct argument
    mock_finder._get_paths.assert_called_once_with(subdirs=False)
