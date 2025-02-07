# file: lib/ansible/cli/playbook.py:61-67
# asked: {"lines": [61, 62, 64, 65, 67], "branches": []}
# gained: {"lines": [61, 62, 64, 65, 67], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.playbook import PlaybookCLI
from ansible.cli import CLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    with patch('ansible.cli.playbook.display', new_callable=Display) as mock_display:
        yield mock_display

@pytest.fixture
def mock_validate_conflicts():
    with patch.object(PlaybookCLI, 'validate_conflicts', autospec=True) as mock_validate:
        yield mock_validate

def test_post_process_args(mock_display, mock_validate_conflicts):
    mock_options = MagicMock()
    mock_options.verbosity = 3

    cli = PlaybookCLI(['arg1', 'arg2'])
    
    with patch.object(CLI, 'post_process_args', return_value=mock_options):
        result = cli.post_process_args(mock_options)

    assert result == mock_options
    assert mock_display.verbosity == 3
    mock_validate_conflicts.assert_called_once_with(cli, mock_options, runas_opts=True, fork_opts=True)
