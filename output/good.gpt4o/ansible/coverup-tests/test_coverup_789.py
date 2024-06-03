# file lib/ansible/context.py:32-35
# lines [32, 35]
# branches []

import pytest
from unittest.mock import patch

# Assuming GlobalCLIArgs is imported from the appropriate module
from ansible.context import _init_global_context, GlobalCLIArgs

@pytest.fixture
def mock_global_cliargs(mocker):
    mock = mocker.patch('ansible.context.GlobalCLIArgs.from_options')
    yield mock
    mocker.stopall()

def test_init_global_context(mock_global_cliargs):
    cli_args = {'some_arg': 'some_value'}
    
    with patch.dict('ansible.context.__dict__', {'CLIARGS': None}):
        _init_global_context(cli_args)
        
        mock_global_cliargs.assert_called_once_with(cli_args)
        from ansible.context import CLIARGS
        assert CLIARGS == mock_global_cliargs.return_value
