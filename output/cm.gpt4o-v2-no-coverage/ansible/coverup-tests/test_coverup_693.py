# file: lib/ansible/cli/playbook.py:61-67
# asked: {"lines": [61, 62, 64, 65, 67], "branches": []}
# gained: {"lines": [61, 62, 64, 65, 67], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.playbook import PlaybookCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    with patch('ansible.cli.playbook.display', new_callable=MagicMock) as mock_display:
        yield mock_display

@pytest.fixture
def mock_validate_conflicts():
    with patch.object(PlaybookCLI, 'validate_conflicts', return_value=None) as mock_method:
        yield mock_method

def test_post_process_args(mock_display, mock_validate_conflicts):
    args = ['test']
    cli = PlaybookCLI(args)
    options = MagicMock()
    options.verbosity = 3

    with patch('ansible.cli.playbook.CLI.post_process_args', return_value=options) as mock_super_method:
        result = cli.post_process_args(options)

    mock_super_method.assert_called_once_with(options)
    assert result == options
    assert mock_display.verbosity == 3
    mock_validate_conflicts.assert_called_once_with(options, runas_opts=True, fork_opts=True)
