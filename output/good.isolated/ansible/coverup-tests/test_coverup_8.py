# file lib/ansible/executor/interpreter_discovery.py:38-162
# lines [38, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 64, 65, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 87, 89, 91, 92, 94, 97, 98, 101, 103, 105, 107, 108, 110, 111, 112, 114, 117, 118, 119, 120, 121, 124, 125, 126, 128, 129, 131, 132, 133, 134, 136, 137, 138, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 156, 157, 160, 161, 162]
# branches ['47->48', '47->50', '74->75', '74->78', '84->85', '84->91', '85->86', '85->89', '91->92', '91->94', '97->98', '97->101', '107->108', '107->110', '111->112', '111->114', '117->118', '117->128', '118->119', '118->128', '119->120', '119->126', '128->129', '128->145', '129->131', '129->136', '131->132', '131->136', '136->137', '136->143', '149->150', '149->155', '152->153', '152->155', '155->156', '155->162']

import json
import pkgutil
import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.interpreter_discovery import discover_interpreter

@pytest.fixture
def action_mock(mocker):
    action = mocker.MagicMock()
    action._low_level_execute_command = mocker.MagicMock()
    action._connection.has_pipelining = True
    action._discovery_warnings = []
    return action

@pytest.fixture
def task_vars():
    return {
        'inventory_hostname': 'testhost',
        'ansible_facts': {}
    }

def test_discover_interpreter_not_linux(action_mock, task_vars):
    # Mock the configuration values
    with patch('ansible.executor.interpreter_discovery.C.config.get_config_value') as get_config_value_mock:
        get_config_value_mock.side_effect = [
            {'centos': {'7': '/usr/bin/python2.7'}},  # INTERPRETER_PYTHON_DISTRO_MAP
            ['/usr/bin/python3', '/usr/bin/python2']  # INTERPRETER_PYTHON_FALLBACK
        ]

        # Mock the uname output to be non-linux
        action_mock._low_level_execute_command.return_value = {
            'stdout': 'PLATFORM\nDarwin\nFOUND\n/usr/bin/python3\nENDFOUND'
        }

        # Run the discovery function
        discover_interpreter(action_mock, 'python', 'auto_silent', task_vars)

        # Check that no warnings were added since it's silent mode
        assert not action_mock._discovery_warnings

def test_discover_interpreter_no_pipelining(action_mock, task_vars):
    # Mock the configuration values
    with patch('ansible.executor.interpreter_discovery.C.config.get_config_value') as get_config_value_mock:
        get_config_value_mock.side_effect = [
            {'centos': {'7': '/usr/bin/python2.7'}},  # INTERPRETER_PYTHON_DISTRO_MAP
            ['/usr/bin/python3', '/usr/bin/python2']  # INTERPRETER_PYTHON_FALLBACK
        ]

        # Mock the uname output to be linux
        action_mock._low_level_execute_command.return_value = {
            'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python3\nENDFOUND'
        }

        # Mock the connection to not support pipelining
        action_mock._connection.has_pipelining = False

        # Run the discovery function
        discover_interpreter(action_mock, 'python', 'auto_silent', task_vars)

        # Check that no warnings were added since it's silent mode
        assert not action_mock._discovery_warnings
