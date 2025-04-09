# file: lib/ansible/cli/doc.py:985-995
# asked: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}
# gained: {"lines": [985, 986, 990, 991, 992, 993, 994, 995], "branches": [[991, 992], [991, 995], [993, 991], [993, 994]]}

import os
from unittest.mock import MagicMock
from ansible.module_utils._text import to_text
from ansible.cli.doc import DocCLI

def test_print_paths():
    # Mock the finder object and its _get_paths method
    finder = MagicMock()
    finder._get_paths.return_value = ['/path/one', '/path/two', '/path/one']

    # Call the static method
    result = DocCLI.print_paths(finder)

    # Verify the result
    expected = os.pathsep.join([to_text('/path/one', errors='surrogate_or_strict'), to_text('/path/two', errors='surrogate_or_strict')])
    assert result == expected

    # Verify that _get_paths was called with the correct arguments
    finder._get_paths.assert_called_once_with(subdirs=False)
