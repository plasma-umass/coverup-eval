# file: lib/ansible/context.py:32-35
# asked: {"lines": [32, 35], "branches": []}
# gained: {"lines": [32, 35], "branches": []}

import pytest
from unittest.mock import patch

# Assuming GlobalCLIArgs is defined somewhere in ansible/context.py
import ansible.context
from ansible.context import _init_global_context, GlobalCLIArgs

@pytest.fixture
def mock_global_cliargs(mocker):
    mock = mocker.patch('ansible.context.GlobalCLIArgs.from_options')
    yield mock
    mock.reset_mock()

def test_init_global_context(mock_global_cliargs, mocker):
    cli_args = {'some_key': 'some_value'}
    
    # Use mocker to patch the global variable CLIARGS
    mocker.patch.dict('ansible.context.__dict__', {'CLIARGS': None})
    
    _init_global_context(cli_args)
    
    mock_global_cliargs.assert_called_once_with(cli_args)
    assert 'CLIARGS' in ansible.context.__dict__
    assert ansible.context.__dict__['CLIARGS'] == mock_global_cliargs.return_value
