# file lib/ansible/cli/doc.py:985-995
# lines [985, 986, 990, 991, 992, 993, 994, 995]
# branches ['991->992', '991->995', '993->991', '993->994']

import pytest
from unittest.mock import MagicMock

def test_print_paths(mocker):
    from ansible.cli.doc import DocCLI

    # Mock the finder object and its _get_paths method
    finder_mock = MagicMock()
    finder_mock._get_paths.return_value = ['/path/one', '/path/two', '/path/one']

    # Call the static method
    result = DocCLI.print_paths(finder_mock)

    # Verify the result
    assert result == '/path/one:/path/two'

    # Verify that _get_paths was called with the correct argument
    finder_mock._get_paths.assert_called_once_with(subdirs=False)
