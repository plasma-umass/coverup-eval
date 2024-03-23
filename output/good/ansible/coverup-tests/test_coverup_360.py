# file lib/ansible/cli/console.py:135-145
# lines [135, 136, 137, 138, 139, 140, 141, 143, 144, 145]
# branches ['139->140', '139->143']

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.utils.color import stringc
import getpass

# Mock the stringc function from ansible.utils.color to simply return the prompt string
@pytest.fixture
def mock_stringc(mocker):
    mocker.patch('ansible.utils.color.stringc', side_effect=lambda x, y, wrap_nonvisible_chars: x)

# Mock the getpass.getuser function to return a fixed username
@pytest.fixture
def mock_getpass(mocker):
    mocker.patch('getpass.getuser', return_value='testuser')

# Mock the inventory and other attributes to test the set_prompt method
@pytest.fixture
def console_cli(mocker, mock_stringc, mock_getpass):
    cli = ConsoleCLI(['ansible-console'])
    cli.inventory = MagicMock()
    cli.inventory.list_hosts.return_value = ['host1', 'host2']
    cli.remote_user = None
    cli.cwd = '/'
    cli.forks = 5
    cli.become = True
    cli.become_user = None
    return cli

def test_set_prompt_become_root(console_cli):
    console_cli.set_prompt()
    assert console_cli.prompt.startswith('testuser@/ (2)[f:5]# ')

def test_set_prompt_become_non_root(console_cli):
    console_cli.become_user = 'nonroot'
    console_cli.set_prompt()
    assert console_cli.prompt.startswith('testuser@/ (2)[f:5]$ ')

def test_set_prompt_non_become(console_cli):
    console_cli.become = False
    console_cli.set_prompt()
    assert console_cli.prompt.startswith('testuser@/ (2)[f:5]$ ')
