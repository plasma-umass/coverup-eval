# file lib/ansible/cli/arguments/option_helpers.py:367-370
# lines [367, 369, 370]
# branches []

# test_option_helpers.py

import pytest
from ansible.cli.arguments.option_helpers import add_tasknoplay_options
from argparse import ArgumentParser
from unittest.mock import MagicMock

# Mock the constant C.TASK_TIMEOUT
@pytest.fixture
def mock_ctask_timeout(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.TASK_TIMEOUT', new=30)

def test_add_tasknoplay_options(mock_ctask_timeout):
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(['--task-timeout', '60'])
    assert args.task_timeout == 60, "The task_timeout should be set to 60"

    # Test the default value
    args = parser.parse_args([])
    assert args.task_timeout == 30, "The task_timeout should be set to the default value of 30"

    # No need to test invalid input with negative or non-integer values as argparse will handle it
    # and the behavior is not part of the function we are testing.
