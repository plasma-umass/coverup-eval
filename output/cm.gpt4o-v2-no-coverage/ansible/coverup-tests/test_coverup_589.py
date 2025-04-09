# file: lib/ansible/cli/arguments/option_helpers.py:283-290
# asked: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}
# gained: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_inventory_options
from ansible import constants as C

def test_add_inventory_options():
    parser = MagicMock()
    add_inventory_options(parser)
    
    parser.add_argument.assert_any_call(
        '-i', '--inventory', '--inventory-file', dest='inventory', action='append',
        help='specify inventory host path or comma separated host list. --inventory-file is deprecated'
    )
    parser.add_argument.assert_any_call(
        '--list-hosts', dest='listhosts', action='store_true',
        help='outputs a list of matching hosts; does not execute anything else'
    )
    parser.add_argument.assert_any_call(
        '-l', '--limit', default=C.DEFAULT_SUBSET, dest='subset',
        help='further limit selected hosts to an additional pattern'
    )
