# file: lib/ansible/cli/arguments/option_helpers.py:232-240
# asked: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}
# gained: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_check_options
from ansible import constants as C

@pytest.fixture
def mock_parser():
    return MagicMock()

def test_add_check_options(mock_parser):
    add_check_options(mock_parser)
    
    # Check that the correct arguments were added to the parser
    mock_parser.add_argument.assert_any_call(
        "-C", "--check", default=False, dest='check', action='store_true',
        help="don't make any changes; instead, try to predict some of the changes that may occur"
    )
    mock_parser.add_argument.assert_any_call(
        '--syntax-check', dest='syntax', action='store_true',
        help="perform a syntax check on the playbook, but do not execute it"
    )
    mock_parser.add_argument.assert_any_call(
        "-D", "--diff", default=C.DIFF_ALWAYS, dest='diff', action='store_true',
        help="when changing (small) files and templates, show the differences in those files; works great with --check"
    )
