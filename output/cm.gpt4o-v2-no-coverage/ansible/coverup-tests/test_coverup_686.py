# file: lib/ansible/cli/arguments/option_helpers.py:216-221
# asked: {"lines": [216, 218, 219, 220, 221], "branches": []}
# gained: {"lines": [216, 218, 219, 220, 221], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_async_options
from ansible import constants as C

def test_add_async_options():
    parser = MagicMock()
    add_async_options(parser)
    
    parser.add_argument.assert_any_call(
        '-P', '--poll', 
        default=C.DEFAULT_POLL_INTERVAL, 
        type=int, 
        dest='poll_interval',
        help="set the poll interval if using -B (default=%s)" % C.DEFAULT_POLL_INTERVAL
    )
    
    parser.add_argument.assert_any_call(
        '-B', '--background', 
        dest='seconds', 
        type=int, 
        default=0,
        help='run asynchronously, failing after X seconds (default=N/A)'
    )
