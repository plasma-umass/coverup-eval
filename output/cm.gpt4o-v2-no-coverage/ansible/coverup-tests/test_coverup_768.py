# file: lib/ansible/cli/arguments/option_helpers.py:277-280
# asked: {"lines": [277, 279, 280], "branches": []}
# gained: {"lines": [277, 279, 280], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_parser():
    return MagicMock()

@patch('ansible.constants.DEFAULT_FORKS', 5)
def test_add_fork_options(mock_parser):
    from ansible.cli.arguments.option_helpers import add_fork_options

    add_fork_options(mock_parser)
    mock_parser.add_argument.assert_called_once_with(
        '-f', '--forks', dest='forks', default=5, type=int,
        help="specify number of parallel processes to use (default=5)"
    )
