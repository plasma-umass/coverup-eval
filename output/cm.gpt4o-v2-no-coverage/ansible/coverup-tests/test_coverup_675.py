# file: lib/ansible/cli/arguments/option_helpers.py:293-298
# asked: {"lines": [293, 295, 296, 297, 298], "branches": []}
# gained: {"lines": [293, 295, 296, 297, 298], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_meta_options
from ansible import constants as C

def test_add_meta_options():
    parser = MagicMock()
    add_meta_options(parser)
    
    parser.add_argument.assert_any_call(
        '--force-handlers',
        default=C.DEFAULT_FORCE_HANDLERS,
        dest='force_handlers',
        action='store_true',
        help='run handlers even if a task fails'
    )
    
    parser.add_argument.assert_any_call(
        '--flush-cache',
        dest='flush_cache',
        action='store_true',
        help='clear the fact cache for every host in inventory'
    )
