# file lib/ansible/cli/arguments/option_helpers.py:210-213
# lines [212, 213]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the module structure is as follows:
# lib/ansible/cli/arguments/option_helpers.py
from ansible.cli.arguments.option_helpers import add_verbosity_options
from ansible.constants import DEFAULT_VERBOSITY

# Test function to cover lines 212-213
def test_add_verbosity_options(mocker):
    # Mock the parser to verify the add_argument call
    mock_parser = MagicMock()
    mock_parser.add_argument = MagicMock()

    # Call the function under test
    add_verbosity_options(mock_parser)

    # Assert that add_argument was called with the correct parameters
    mock_parser.add_argument.assert_called_with(
        '-v', '--verbose', dest='verbosity', default=DEFAULT_VERBOSITY, action="count",
        help="verbose mode (-vvv for more, -vvvv to enable connection debugging)"
    )
