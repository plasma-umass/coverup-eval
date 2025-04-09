# file: lib/ansible/cli/arguments/option_helpers.py:224-229
# asked: {"lines": [224, 226, 227, 229], "branches": []}
# gained: {"lines": [224, 226, 227, 229], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_basedir_options

@pytest.fixture
def mock_parser():
    return MagicMock()

@patch('ansible.cli.arguments.option_helpers.C')
@patch('ansible.cli.arguments.option_helpers.unfrack_path')
def test_add_basedir_options(mock_unfrack_path, mock_constants, mock_parser):
    mock_constants.config.get_config_value.return_value = 'mock_playbook_dir'
    mock_unfrack_path.return_value = 'mock_unfrack_path'

    add_basedir_options(mock_parser)

    mock_parser.add_argument.assert_called_once_with(
        '--playbook-dir',
        default='mock_playbook_dir',
        dest='basedir',
        action='store',
        help="Since this tool does not use playbooks, use this as a substitute playbook directory."
             "This sets the relative path for many features including roles/ group_vars/ etc.",
        type='mock_unfrack_path'
    )
