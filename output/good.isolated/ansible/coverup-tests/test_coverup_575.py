# file lib/ansible/cli/arguments/option_helpers.py:41-47
# lines [41, 42, 43, 44, 46, 47]
# branches []

import argparse
import pytest
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument_action(mocker):
    # Mock the parser to verify that parser.error is called with the correct message
    mock_parser = mocker.Mock()
    mock_parser.error.side_effect = argparse.ArgumentError(None, 'unrecognized arguments: --foo')

    # Create the UnrecognizedArgument instance
    action = UnrecognizedArgument(option_strings=['--foo'], dest='bar')

    # Call the action with a mock parser and verify the error is called
    with pytest.raises(argparse.ArgumentError) as excinfo:
        action.__call__(parser=mock_parser, namespace=mocker.Mock(), values=None, option_string='--foo')
    
    # Assert that the exception message is correct
    assert str(excinfo.value) == 'unrecognized arguments: --foo'
