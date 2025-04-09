# file lib/ansible/cli/arguments/option_helpers.py:301-306
# lines [303, 304, 305, 306]
# branches []

import pytest
from unittest import mock
from ansible.cli.arguments.option_helpers import add_module_options
from argparse import ArgumentParser

@pytest.fixture
def mock_config(mocker):
    mock_config = mocker.patch('ansible.cli.arguments.option_helpers.C.config.get_configuration_definition')
    mock_config.return_value = {'default': '/default/module/path'}
    return mock_config

def test_add_module_options(mock_config):
    parser = ArgumentParser()
    add_module_options(parser)
    
    args = parser.parse_args(['--module-path', '/custom/module/path'])
    
    assert args.module_path == ['/custom/module/path']

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
