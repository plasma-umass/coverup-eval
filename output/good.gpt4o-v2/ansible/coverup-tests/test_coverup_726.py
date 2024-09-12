# file: lib/ansible/cli/arguments/option_helpers.py:277-280
# asked: {"lines": [277, 279, 280], "branches": []}
# gained: {"lines": [277, 279, 280], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_fork_options
from ansible import constants as C

def test_add_fork_options():
    parser = MagicMock()
    add_fork_options(parser)
    parser.add_argument.assert_called_once_with(
        '-f', '--forks', dest='forks', default=C.DEFAULT_FORKS, type=int,
        help="specify number of parallel processes to use (default=%s)" % C.DEFAULT_FORKS
    )
