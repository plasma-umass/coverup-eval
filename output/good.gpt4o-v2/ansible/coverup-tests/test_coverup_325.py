# file: lib/ansible/cli/doc.py:985-995
# asked: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}
# gained: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.doc import DocCLI

def test_print_paths():
    # Mock the finder object
    finder = MagicMock()
    finder._get_paths.return_value = ['/path/one', '/path/two', '/path/one']

    # Call the static method
    result = DocCLI.print_paths(finder)

    # Verify the result
    assert result == '/path/one:/path/two'

    # Verify the _get_paths method was called with the correct arguments
    finder._get_paths.assert_called_once_with(subdirs=False)
