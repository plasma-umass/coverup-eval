# file lib/ansible/cli/arguments/option_helpers.py:309-314
# lines [309, 311, 312, 313, 314]
# branches []

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_output_options

# Test function to improve coverage for add_output_options
def test_add_output_options(mocker):
    # Create a mock ArgumentParser
    mock_parser = mocker.MagicMock(spec=ArgumentParser)

    # Call the function to test
    add_output_options(mock_parser)

    # Assert that add_argument was called with the expected parameters for '--one-line'
    mock_parser.add_argument.assert_any_call(
        '-o', '--one-line', dest='one_line', action='store_true', help='condense output'
    )

    # Assert that add_argument was called with the expected parameters for '--tree'
    mock_parser.add_argument.assert_any_call(
        '-t', '--tree', dest='tree', default=None, help='log output to this directory'
    )

    # Assert that add_argument was called exactly 2 times
    assert mock_parser.add_argument.call_count == 2

    # Clean up by removing any side effects on the mock
    mocker.stopall()
