# file: lib/ansible/cli/doc.py:985-995
# asked: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}
# gained: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.doc import DocCLI
import os

def test_print_paths(monkeypatch):
    # Mock the finder object and its _get_paths method
    mock_finder = MagicMock()
    mock_finder._get_paths.return_value = ['/path/one', '/path/two', '/path/one']

    # Call the static method
    result = DocCLI.print_paths(mock_finder)

    # Verify the result
    expected_result = os.pathsep.join(['/path/one', '/path/two'])
    assert result == expected_result

    # Ensure _get_paths was called with the correct arguments
    mock_finder._get_paths.assert_called_once_with(subdirs=False)
