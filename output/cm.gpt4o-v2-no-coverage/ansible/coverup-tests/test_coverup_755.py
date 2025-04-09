# file: lib/ansible/cli/arguments/option_helpers.py:210-213
# asked: {"lines": [210, 212, 213], "branches": []}
# gained: {"lines": [210, 212, 213], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.cli.arguments.option_helpers import add_verbosity_options
from ansible import constants as C

def test_add_verbosity_options():
    parser = MagicMock()
    add_verbosity_options(parser)
    
    parser.add_argument.assert_called_once_with(
        '-v', '--verbose', dest='verbosity', default=C.DEFAULT_VERBOSITY, action='count',
        help='verbose mode (-vvv for more, -vvvv to enable connection debugging)'
    )
