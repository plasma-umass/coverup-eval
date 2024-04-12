# file lib/ansible/plugins/action/include_vars.py:48-70
# lines [48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70]
# branches ['55->56', '55->60', '57->58', '57->60', '67->68', '67->69', '69->exit', '69->70']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action import include_vars
from ansible.utils.sentinel import Sentinel
from unittest.mock import MagicMock

# Mocking string_types for the test as it is not defined in the provided code snippet
include_vars.string_types = (str,)

@pytest.fixture
def action_include_vars():
    mock_loader = MagicMock()
    mock_loader.get_real_file = MagicMock()
    task = MagicMock()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    fake_display = MagicMock()
    return include_vars.ActionModule(task, connection, play_context, mock_loader, fake_display, Sentinel)

def test_action_include_vars_with_invalid_extensions_type(action_include_vars, mocker):
    mocker.patch.object(action_include_vars, '_task', create=True)
    action_include_vars._task.args = {
        'extensions': 123  # Invalid type, should be a list or a string
    }
    with pytest.raises(AnsibleError):
        action_include_vars._set_args()

def test_action_include_vars_with_string_extensions(action_include_vars, mocker):
    mocker.patch.object(action_include_vars, '_task', create=True)
    action_include_vars._task.args = {
        'extensions': 'txt'  # String type, should be converted to a list
    }
    action_include_vars._set_args()
    assert action_include_vars.valid_extensions == ['t', 'x', 't']  # String is converted to list of characters

def test_action_include_vars_with_list_extensions(action_include_vars, mocker):
    mocker.patch.object(action_include_vars, '_task', create=True)
    action_include_vars._task.args = {
        'extensions': ['txt', 'yaml']  # List type, should remain a list
    }
    action_include_vars._set_args()
    assert action_include_vars.valid_extensions == ['txt', 'yaml']  # List remains unchanged

def test_action_include_vars_without_source(action_include_vars, mocker):
    mocker.patch.object(action_include_vars, '_task', create=True)
    action_include_vars._task.args = {
        '_raw_params': 'vars_file.yml\n'  # Simulate raw params with trailing newline
    }
    action_include_vars._set_args()
    assert action_include_vars.source_file == 'vars_file.yml'  # Trailing newline should be stripped
