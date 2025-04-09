# file lib/ansible/cli/console.py:115-119
# lines [116, 117, 118, 119]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import MagicMock, patch

# Test function to cover lines 116-119
def test_post_process_args(mocker):
    # Mock the display object to avoid side effects
    mock_display = mocker.patch('ansible.cli.console.display')

    # Create a mock options object
    mock_options = MagicMock()
    mock_options.verbosity = 0

    # Mock the super().post_process_args method to return the mock options object
    with patch('ansible.cli.console.CLI.post_process_args', return_value=mock_options) as mock_super_post_process_args:
        # Create an instance of ConsoleCLI with a dummy argument to avoid ValueError
        console_cli = ConsoleCLI(['dummy_arg'])

        # Mock the validate_conflicts method to avoid side effects
        console_cli.validate_conflicts = MagicMock()

        # Call post_process_args to execute lines 116-119
        options = console_cli.post_process_args(mock_options)

        # Assertions to verify postconditions
        mock_super_post_process_args.assert_called_once_with(mock_options)
        assert mock_display.verbosity == mock_options.verbosity
        assert options is mock_options

        # Verify that validate_conflicts was called with the correct arguments
        console_cli.validate_conflicts.assert_called_once_with(mock_options, runas_opts=True, fork_opts=True)
