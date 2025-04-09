# file lib/ansible/cli/arguments/option_helpers.py:224-229
# lines [224, 226, 227, 229]
# branches []

import pytest
from unittest import mock
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_basedir_options

@pytest.fixture
def mock_config(mocker):
    mock_config = mocker.patch('ansible.cli.arguments.option_helpers.C')
    mock_config.config.get_config_value.return_value = '/default/playbook/dir'
    return mock_config

def test_add_basedir_options(mock_config):
    parser = ArgumentParser()
    add_basedir_options(parser)
    args = parser.parse_args(['--playbook-dir', '/custom/playbook/dir'])
    
    assert args.basedir == '/custom/playbook/dir'
    mock_config.config.get_config_value.assert_called_once_with('PLAYBOOK_DIR')

def test_add_basedir_options_default(mock_config):
    parser = ArgumentParser()
    add_basedir_options(parser)
    args = parser.parse_args([])
    
    assert args.basedir == '/default/playbook/dir'
    mock_config.config.get_config_value.assert_called_once_with('PLAYBOOK_DIR')
