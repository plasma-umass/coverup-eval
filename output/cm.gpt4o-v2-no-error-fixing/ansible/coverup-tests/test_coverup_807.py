# file: lib/ansible/cli/arguments/option_helpers.py:224-229
# asked: {"lines": [226, 227, 229], "branches": []}
# gained: {"lines": [226, 227, 229], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_basedir_options

@pytest.fixture
def mock_parser():
    return MagicMock()

@patch('ansible.cli.arguments.option_helpers.C.config.get_config_value')
@patch('ansible.cli.arguments.option_helpers.unfrack_path')
def test_add_basedir_options(mock_unfrack_path, mock_get_config_value, mock_parser):
    mock_get_config_value.return_value = '/default/path'
    mock_unfrack_path.return_value = '/unfracked/path'

    add_basedir_options(mock_parser)

    mock_parser.add_argument.assert_called_once_with(
        '--playbook-dir',
        default='/default/path',
        dest='basedir',
        action='store',
        help="Since this tool does not use playbooks, use this as a substitute playbook directory."
             "This sets the relative path for many features including roles/ group_vars/ etc.",
        type='/unfracked/path'
    )
