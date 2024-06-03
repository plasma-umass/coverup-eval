# file lib/ansible/cli/adhoc.py:56-64
# lines [59, 61, 62, 64]
# branches []

import pytest
from unittest import mock
from ansible.cli.adhoc import AdHocCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.adhoc.display', new_callable=Display)

@pytest.fixture
def mock_super_post_process_args(mocker):
    return mocker.patch('ansible.cli.adhoc.CLI.post_process_args', return_value=mock.Mock(verbosity=3, forks=1))

def test_post_process_args(mock_display, mock_super_post_process_args):
    args = mock.Mock()
    adhoc_cli = AdHocCLI(args)
    options = mock.Mock(forks=1)
    
    processed_options = adhoc_cli.post_process_args(options)
    
    mock_super_post_process_args.assert_called_once_with(options)
    assert mock_display.verbosity == 3
    assert processed_options == mock_super_post_process_args.return_value
