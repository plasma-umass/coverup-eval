# file: lib/ansible/cli/adhoc.py:56-64
# asked: {"lines": [56, 59, 61, 62, 64], "branches": []}
# gained: {"lines": [56, 59, 61, 62, 64], "branches": []}

import pytest
from unittest import mock
from ansible.cli.adhoc import AdHocCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    with mock.patch('ansible.cli.adhoc.display', new_callable=Display) as mock_display:
        yield mock_display

@pytest.fixture
def mock_super_post_process_args():
    with mock.patch('ansible.cli.adhoc.CLI.post_process_args', return_value=mock.Mock(verbosity=3)) as mock_method:
        yield mock_method

@pytest.fixture
def mock_validate_conflicts():
    with mock.patch.object(AdHocCLI, 'validate_conflicts') as mock_method:
        yield mock_method

def test_post_process_args(mock_display, mock_super_post_process_args, mock_validate_conflicts):
    cli = AdHocCLI(args=['test'])
    options = mock.Mock()
    options.verbosity = 0

    processed_options = cli.post_process_args(options)

    mock_super_post_process_args.assert_called_once_with(options)
    assert mock_display.verbosity == 3
    mock_validate_conflicts.assert_called_once_with(processed_options, runas_opts=True, fork_opts=True)
    assert processed_options == mock_super_post_process_args.return_value
