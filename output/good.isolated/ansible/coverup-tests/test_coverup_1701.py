# file lib/ansible/cli/arguments/option_helpers.py:28-31
# lines [30, 31]
# branches []

import argparse
import operator
import pytest
from ansible.cli.arguments.option_helpers import SortingHelpFormatter

def test_sorting_help_formatter_add_arguments(mocker):
    # Mock the super().add_arguments method to track if it's called with sorted actions
    mock_super_add_arguments = mocker.patch.object(argparse.HelpFormatter, 'add_arguments')

    # Create a SortingHelpFormatter instance
    formatter = SortingHelpFormatter(prog='test')

    # Create mock actions with out-of-order option_strings
    action1 = mocker.Mock()
    action1.option_strings = ['--second']
    action2 = mocker.Mock()
    action2.option_strings = ['--first']
    actions = [action1, action2]

    # Call the add_arguments method
    formatter.add_arguments(actions)

    # Check if the actions were sorted before being passed to super().add_arguments
    args, kwargs = mock_super_add_arguments.call_args
    sorted_actions = args[0]
    assert sorted_actions == [action2, action1], "Actions were not sorted correctly"

    # Check if the super().add_arguments was called once
    mock_super_add_arguments.assert_called_once()
