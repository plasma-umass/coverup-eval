# file: lib/ansible/cli/arguments/option_helpers.py:361-364
# asked: {"lines": [361, 363, 364], "branches": []}
# gained: {"lines": [361, 363, 364], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming maybe_unfrack_path is defined somewhere in the module
from ansible.cli.arguments.option_helpers import add_runtask_options

def test_add_runtask_options(monkeypatch):
    parser = MagicMock()
    maybe_unfrack_path = MagicMock(return_value=lambda x: x)
    
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.maybe_unfrack_path', maybe_unfrack_path)
    
    add_runtask_options(parser)
    
    parser.add_argument.assert_called_with(
        '-e', '--extra-vars', dest="extra_vars", action="append", type=maybe_unfrack_path('@'),
        help="set additional variables as key=value or YAML/JSON, if filename prepend with @", default=[]
    )
