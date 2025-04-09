# file: lib/ansible/cli/adhoc.py:56-64
# asked: {"lines": [56, 59, 61, 62, 64], "branches": []}
# gained: {"lines": [56, 59, 61, 62, 64], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming AdHocCLI and CLI are imported from ansible.cli.adhoc and ansible.cli respectively
from ansible.cli.adhoc import AdHocCLI
from ansible.cli import CLI

class TestAdHocCLI:
    
    @patch('ansible.cli.adhoc.display')
    def test_post_process_args(self, mock_display):
        # Mock the options object
        options = MagicMock()
        options.verbosity = 3
        
        # Create an instance of AdHocCLI
        adhoc_cli = AdHocCLI(args=['test'])
        
        # Mock the parent class's post_process_args method
        with patch.object(CLI, 'post_process_args', return_value=options) as mock_super_post_process_args:
            # Mock the validate_conflicts method
            with patch.object(AdHocCLI, 'validate_conflicts') as mock_validate_conflicts:
                # Call the method under test
                result = adhoc_cli.post_process_args(options)
                
                # Assertions
                mock_super_post_process_args.assert_called_once_with(options)
                mock_display.verbosity = options.verbosity
                mock_validate_conflicts.assert_called_once_with(options, runas_opts=True, fork_opts=True)
                assert result == options
