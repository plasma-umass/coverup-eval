# file lib/ansible/cli/arguments/option_helpers.py:28-31
# lines [30, 31]
# branches []

import argparse
import operator
import pytest
from unittest import mock

# Assuming the SortingHelpFormatter class is defined in ansible.cli.arguments.option_helpers
from ansible.cli.arguments.option_helpers import SortingHelpFormatter

def test_sorting_help_formatter_add_arguments(mocker):
    # Create a mock for the super class's add_arguments method
    mock_super_add_arguments = mocker.patch.object(argparse.HelpFormatter, 'add_arguments')

    # Create a list of mock actions with option_strings attributes
    action1 = mock.Mock(option_strings=['--beta'])
    action2 = mock.Mock(option_strings=['--alpha'])
    actions = [action1, action2]

    # Instantiate the SortingHelpFormatter
    formatter = SortingHelpFormatter(prog='test')

    # Call the add_arguments method
    formatter.add_arguments(actions)

    # Check that the actions were sorted correctly
    sorted_actions = sorted(actions, key=operator.attrgetter('option_strings'))
    mock_super_add_arguments.assert_called_once_with(sorted_actions)

    # Ensure the original actions list is not modified
    assert actions == [action1, action2]

# Note: pytest-mock is used to mock the super class's add_arguments method
