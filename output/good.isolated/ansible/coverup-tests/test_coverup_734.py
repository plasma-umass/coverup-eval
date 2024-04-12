# file lib/ansible/cli/console.py:398-401
# lines [398, 400, 401]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch
from io import StringIO

# Test function to cover do_exit method
def test_do_exit_method(mocker):
    mocker.patch('ansible.cli.CLI.__init__', return_value=None)
    console_cli = ConsoleCLI(['console'])

    # Patch sys.stdout to capture output for assertion
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        # Call the do_exit method
        exit_code = console_cli.do_exit(None)

        # Check if the correct message is printed to stdout
        assert mock_stdout.getvalue() == '\nAnsible-console was exited.\n'

        # Check if the method returns -1
        assert exit_code == -1
