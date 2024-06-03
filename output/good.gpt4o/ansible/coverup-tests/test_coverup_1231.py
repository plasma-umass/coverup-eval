# file lib/ansible/cli/console.py:115-119
# lines [116, 117, 118, 119]
# branches []

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.console.display', new_callable=Display)

@pytest.fixture
def mock_super_post_process_args(mocker):
    return mocker.patch('ansible.cli.console.CLI.post_process_args', return_value=mock.Mock(verbosity=3))

@pytest.fixture
def mock_validate_conflicts(mocker):
    return mocker.patch.object(ConsoleCLI, 'validate_conflicts')

def test_post_process_args(mock_display, mock_super_post_process_args, mock_validate_conflicts):
    cli = ConsoleCLI(args=['test'])
    options = mock.Mock()
    
    result = cli.post_process_args(options)
    
    mock_super_post_process_args.assert_called_once_with(options)
    assert mock_display.verbosity == 3
    mock_validate_conflicts.assert_called_once_with(mock_super_post_process_args.return_value, runas_opts=True, fork_opts=True)
    assert result == mock_super_post_process_args.return_value
