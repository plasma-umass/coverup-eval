# file: lib/ansible/cli/arguments/option_helpers.py:309-314
# asked: {"lines": [309, 311, 312, 313, 314], "branches": []}
# gained: {"lines": [309, 311, 312, 313, 314], "branches": []}

import pytest
from unittest.mock import MagicMock

def test_add_output_options():
    from ansible.cli.arguments.option_helpers import add_output_options

    # Create a mock parser object
    parser = MagicMock()

    # Call the function with the mock parser
    add_output_options(parser)

    # Assert that add_argument was called with the expected arguments
    parser.add_argument.assert_any_call('-o', '--one-line', dest='one_line', action='store_true', help='condense output')
    parser.add_argument.assert_any_call('-t', '--tree', dest='tree', default=None, help='log output to this directory')
