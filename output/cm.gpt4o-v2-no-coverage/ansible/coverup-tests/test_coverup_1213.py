# file: lib/ansible/context.py:32-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
from ansible.utils.context_objects import GlobalCLIArgs
from ansible.context import _init_global_context

@pytest.fixture
def mock_cli_args(mocker):
    mock_options = mocker.Mock()
    mock_options.some_option = 'some_value'
    return mock_options

def test_init_global_context(mock_cli_args, mocker):
    mocker.patch('ansible.utils.context_objects.GlobalCLIArgs.from_options', return_value=GlobalCLIArgs({'some_option': 'some_value'}))
    
    _init_global_context(mock_cli_args)
    
    from ansible.context import CLIARGS
    assert CLIARGS['some_option'] == 'some_value'
