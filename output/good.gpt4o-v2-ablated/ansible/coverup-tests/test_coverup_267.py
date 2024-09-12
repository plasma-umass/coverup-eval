# file: lib/ansible/cli/arguments/option_helpers.py:224-229
# asked: {"lines": [224, 226, 227, 229], "branches": []}
# gained: {"lines": [224, 226, 227, 229], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_basedir_options

@pytest.fixture
def mock_parser():
    return MagicMock()

@pytest.fixture
def mock_config():
    with patch('ansible.cli.arguments.option_helpers.C.config.get_config_value') as mock_config:
        yield mock_config

@pytest.fixture
def mock_unfrack_path():
    with patch('ansible.cli.arguments.option_helpers.unfrack_path') as mock_unfrack_path:
        yield mock_unfrack_path

def test_add_basedir_options(mock_parser, mock_config, mock_unfrack_path):
    mock_config.return_value = '/default/playbook/dir'
    mock_unfrack_path.return_value = lambda x: x

    add_basedir_options(mock_parser)

    mock_parser.add_argument.assert_called_once_with(
        '--playbook-dir',
        default='/default/playbook/dir',
        dest='basedir',
        action='store',
        help="Since this tool does not use playbooks, use this as a substitute playbook directory."
             "This sets the relative path for many features including roles/ group_vars/ etc.",
        type=mock_unfrack_path()
    )
