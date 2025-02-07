# file: lib/ansible/cli/arguments/option_helpers.py:317-337
# asked: {"lines": [317, 324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}
# gained: {"lines": [317, 324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.cli.arguments.option_helpers import add_runas_options

def test_add_runas_options():
    parser = Mock()
    parser.add_argument_group = Mock()
    parser.add_mutually_exclusive_group = Mock()

    add_runas_options(parser)

    parser.add_argument_group.assert_called()
    assert parser.add_argument_group.call_count == 3

    runas_group = parser.add_argument_group.call_args_list[0][0][0]
    assert runas_group == "Privilege Escalation Options"

    runas_pass_group = parser.add_argument_group.call_args_list[2][0][0]
    assert runas_pass_group is not None

    parser.add_mutually_exclusive_group.assert_called_once()
