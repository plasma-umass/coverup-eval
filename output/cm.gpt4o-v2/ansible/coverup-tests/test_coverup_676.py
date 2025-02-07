# file: lib/ansible/cli/arguments/option_helpers.py:301-306
# asked: {"lines": [301, 303, 304, 305, 306], "branches": []}
# gained: {"lines": [301, 303, 304, 305, 306], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_module_options
from ansible.cli.arguments.option_helpers import PrependListAction
from ansible.utils.path import unfrackpath

def unfrack_path(pathsep=False):
    """Turn an Option's data into a single path in Ansible locations"""

    def inner(value):
        if pathsep:
            return [unfrackpath(x) for x in value.split(os.pathsep) if x]
        if value == '-':
            return value
        return unfrackpath(value)
    return inner

@pytest.fixture
def mock_parser():
    parser = ArgumentParser()
    return parser

@pytest.fixture
def mock_config():
    with patch('ansible.constants.config.get_configuration_definition') as mock_config:
        mock_config.return_value = {'default': '/default/module/path'}
        yield mock_config

def test_add_module_options(mock_parser, mock_config):
    add_module_options(mock_parser)
    args = mock_parser.parse_args(['--module-path', '/custom/module/path'])
    assert args.module_path == ['/custom/module/path']

    args = mock_parser.parse_args(['--module-path', '/default/module/path'])
    assert args.module_path == ['/default/module/path']
