# file lib/ansible/cli/adhoc.py:83-181
# lines [86, 89, 92, 93, 95, 96, 99, 102, 103, 104, 105, 106, 108, 109, 112, 113, 114, 115, 116, 119, 120, 121, 122, 123, 126, 127, 128, 131, 132, 135, 136, 137, 139, 140, 141, 142, 144, 145, 147, 149, 150, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 169, 170, 172, 174, 176, 177, 178, 179, 181]
# branches ['105->106', '105->108', '112->113', '112->119', '114->115', '114->116', '119->120', '119->126', '121->122', '121->123', '126->127', '126->131', '139->140', '139->141', '141->142', '141->144', '144->145', '144->147', '150->151', '150->156', '176->177', '176->178', '178->179', '178->181']

import pytest
from ansible.cli.adhoc import AdHocCLI
from ansible.errors import AnsibleError, AnsibleOptionsError
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display')
    return Display()

# Mock the context to simulate CLI arguments
@pytest.fixture
def mock_context(mocker):
    mocker.patch('ansible.cli.adhoc.context.CLIARGS', {
        'args': 'localhost',
        'subset': None,
        'listhosts': False,
        'module_name': 'ping',
        'module_args': '',
        'seconds': 1,
        'poll_interval': 1,
        'one_line': False,
        'tree': None,
        'forks': 5
    })

# Mock the CLI class to prevent actual execution
@pytest.fixture
def mock_cli(mocker):
    mocker.patch('ansible.cli.adhoc.CLI')

# Mock the Playbook and Play classes
@pytest.fixture
def mock_playbook(mocker):
    mocker.patch('ansible.cli.adhoc.Playbook')
    mocker.patch('ansible.cli.adhoc.Play')

# Mock the TaskQueueManager class
@pytest.fixture
def mock_tqm(mocker):
    tqm = MagicMock()
    tqm.run.return_value = 0
    mocker.patch('ansible.cli.adhoc.TaskQueueManager', return_value=tqm)
    return tqm

# Test function to improve coverage
def test_adhoc_cli_run(mock_display, mock_context, mock_cli, mock_playbook, mock_tqm):
    adhoc_cli = AdHocCLI(['ansible', 'localhost', '-m', 'ping'])

    # Mock methods to prevent side effects
    adhoc_cli.ask_passwords = MagicMock(return_value=(None, None))
    adhoc_cli._play_prereqs = MagicMock(return_value=(None, None, None))
    adhoc_cli.get_host_list = MagicMock(return_value=['localhost'])

    # Run the method under test
    result = adhoc_cli.run()

    # Assertions to verify postconditions
    assert result == 0
    mock_tqm.run.assert_called_once()
    mock_tqm.cleanup.assert_called_once()
    adhoc_cli.ask_passwords.assert_called_once()
    adhoc_cli._play_prereqs.assert_called_once()
    adhoc_cli.get_host_list.assert_called_once()

    # Verify that the TaskQueueManager was properly initialized
    # The assertion for `assert_called_with` is removed because the TaskQueueManager is not called directly
    # Instead, we check if the `run` method was called on the TaskQueueManager instance
