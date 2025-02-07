# file: lib/ansible/cli/adhoc.py:56-64
# asked: {"lines": [56, 59, 61, 62, 64], "branches": []}
# gained: {"lines": [56, 59, 61, 62, 64], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.adhoc import AdHocCLI
from ansible.cli import CLI

class MockOptions:
    def __init__(self, verbosity):
        self.verbosity = verbosity

@pytest.fixture
def mock_options():
    return MockOptions(verbosity=3)

@pytest.fixture
def adhoc_cli():
    return AdHocCLI(args=['test'])

def test_post_process_args(monkeypatch, adhoc_cli, mock_options):
    # Mock the super class method
    mock_super_post_process_args = MagicMock(return_value=mock_options)
    monkeypatch.setattr(CLI, 'post_process_args', mock_super_post_process_args)
    
    # Mock the display object
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.cli.adhoc.display', mock_display)
    
    # Mock the validate_conflicts method
    mock_validate_conflicts = MagicMock()
    monkeypatch.setattr(AdHocCLI, 'validate_conflicts', mock_validate_conflicts)
    
    # Call the method
    result = adhoc_cli.post_process_args(mock_options)
    
    # Assertions
    mock_super_post_process_args.assert_called_once_with(mock_options)
    assert mock_display.verbosity == mock_options.verbosity
    mock_validate_conflicts.assert_called_once_with(mock_options, runas_opts=True, fork_opts=True)
    assert result == mock_options
