# file lib/ansible/cli/console.py:398-401
# lines [398, 400, 401]
# branches []

import pytest
from unittest import mock
import sys
from ansible.cli.console import ConsoleCLI

def test_do_exit(mocker):
    # Mock sys.stdout to capture the output
    mock_stdout = mocker.patch('sys.stdout', new_callable=mock.MagicMock)
    
    # Mock the args required for ConsoleCLI initialization
    mock_args = mocker.Mock()
    
    # Create an instance of ConsoleCLI with the mocked args
    console_cli = ConsoleCLI(mock_args)
    
    # Call the do_exit method
    result = console_cli.do_exit(None)
    
    # Assert that the correct message was written to stdout
    mock_stdout.write.assert_called_once_with('\nAnsible-console was exited.\n')
    
    # Assert that the method returns -1
    assert result == -1
