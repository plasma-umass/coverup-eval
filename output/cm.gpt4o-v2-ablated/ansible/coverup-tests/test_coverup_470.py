# file: lib/ansible/context.py:32-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
from unittest.mock import patch

# Assuming GlobalCLIArgs is defined somewhere in ansible/context.py
from ansible.context import _init_global_context, GlobalCLIArgs

@pytest.fixture
def mock_global_cliargs(mocker):
    mocker.patch('ansible.context.GlobalCLIArgs.from_options', return_value='mocked_cliargs')
    yield
    # Cleanup if necessary

def test_init_global_context(mock_global_cliargs):
    cli_args = {'some': 'args'}
    _init_global_context(cli_args)
    
    from ansible.context import CLIARGS
    assert CLIARGS == 'mocked_cliargs'
