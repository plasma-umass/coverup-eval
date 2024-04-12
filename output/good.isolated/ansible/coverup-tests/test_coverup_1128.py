# file lib/ansible/executor/interpreter_discovery.py:38-162
# lines [48, 75, 76, 85, 86, 87, 89, 98, 103, 105, 107, 108, 110, 111, 112, 114, 117, 118, 119, 120, 121, 124, 125, 126, 128, 129, 131, 132, 133, 134, 136, 137, 138, 141, 142, 143, 145, 148, 149, 150, 151, 152, 153, 156, 157, 160, 161]
# branches ['47->48', '74->75', '84->85', '85->86', '85->89', '97->98', '107->108', '107->110', '111->112', '111->114', '117->118', '117->128', '118->119', '118->128', '119->120', '119->126', '128->129', '128->145', '129->131', '129->136', '131->132', '131->136', '136->137', '136->143', '149->150', '149->155', '152->153', '152->155', '155->156']

import json
import pkgutil
import pytest
from ansible.executor.interpreter_discovery import discover_interpreter
from ansible.module_utils._text import to_text
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'vvv')
    mocker.patch.object(Display, 'debug')
    mocker.patch.object(Display, 'warning')

# Mock the action plugin with the necessary attributes and methods
@pytest.fixture
def mock_action(mocker):
    action = MagicMock()
    action._low_level_execute_command = MagicMock()
    action._connection = MagicMock()
    action._connection.has_pipelining = True
    action._discovery_warnings = []
    return action

# Mock the configuration values
@pytest.fixture
def mock_config(mocker):
    mocker.patch('ansible.config.manager.ConfigManager.get_config_value', side_effect=lambda x, variables: {
        'INTERPRETER_PYTHON_DISTRO_MAP': {'linux': {'default': '/usr/bin/python3'}},
        'INTERPRETER_PYTHON_FALLBACK': ['/usr/bin/python3', '/usr/bin/python']
    }.get(x))

# Mock the pkgutil.get_data to return a dummy script
@pytest.fixture
def mock_pkgutil(mocker):
    mocker.patch('pkgutil.get_data', return_value=b'print(json.dumps({"os_release": {"NAME": "Linux", "VERSION_ID": "default"}}))')

# Mock the json.loads to handle the dummy script output
@pytest.fixture
def mock_json_loads(mocker):
    mocker.patch('json.loads', return_value={"os_release": {"NAME": "Linux", "VERSION_ID": "default"}})

# Test function to cover the missing lines
def test_discover_interpreter(mock_action, mock_display, mock_config, mock_pkgutil, mock_json_loads):
    task_vars = {
        'inventory_hostname': 'testhost',
        'ansible_python_interpreter': '/usr/bin/python3'
    }
    mock_action._low_level_execute_command.return_value = {
        'stdout': 'PLATFORM\nlinux\nFOUND\n/usr/bin/python3\nENDFOUND',
        'stderr': ''
    }

    # Call the function with the mocked objects
    interpreter = discover_interpreter(mock_action, 'python', 'auto_silent', task_vars)

    # Assertions to check postconditions
    assert interpreter == '/usr/bin/python3'
    assert mock_action._low_level_execute_command.called
    assert not mock_action._discovery_warnings  # No warnings should be present
