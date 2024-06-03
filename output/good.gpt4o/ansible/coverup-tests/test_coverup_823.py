# file lib/ansible/cli/adhoc.py:23-27
# lines [23, 24]
# branches []

import pytest
from ansible.cli.adhoc import AdHocCLI
from ansible.cli import CLI

def test_adhoc_cli_initialization(mocker):
    # Mock the required 'args' argument for CLI initialization
    mock_args = mocker.patch('ansible.cli.CLI.__init__', return_value=None)

    # Test that AdHocCLI can be instantiated and is a subclass of CLI
    adhoc_cli = AdHocCLI([])
    assert isinstance(adhoc_cli, AdHocCLI)
    assert isinstance(adhoc_cli, CLI)
