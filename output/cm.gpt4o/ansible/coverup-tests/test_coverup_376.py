# file lib/ansible/cli/arguments/option_helpers.py:317-337
# lines [317, 324, 327, 328, 329, 330, 331, 332, 333, 335, 337]
# branches []

import pytest
from unittest import mock
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_options

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_BECOME', True)
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_BECOME_METHOD', 'sudo')
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_BECOME_USER', 'root')

def test_add_runas_options(mock_constants):
    parser = ArgumentParser()
    add_runas_options(parser)
    
    args = parser.parse_args(['-b', '--become-method', 'sudo', '--become-user', 'admin'])
    
    assert args.become is True
    assert args.become_method == 'sudo'
    assert args.become_user == 'admin'
