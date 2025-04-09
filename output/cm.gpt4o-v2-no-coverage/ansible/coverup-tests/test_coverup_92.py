# file: lib/ansible/plugins/action/gather_facts.py:19-53
# asked: {"lines": [19, 21, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 41, 44, 45, 46, 48, 49, 50, 53], "branches": [[24, 26], [24, 41], [26, 27], [26, 31], [28, 29], [28, 31], [32, 33], [32, 35], [36, 37], [36, 41]]}
# gained: {"lines": [19, 21, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 41, 44, 45, 46, 48, 49, 50, 53], "branches": [[24, 26], [24, 41], [26, 27], [26, 31], [28, 29], [32, 33], [36, 37]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.gather_facts import ActionModule
from ansible.executor.module_common import get_action_args_with_defaults

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {
        'gather_subset': 'test_subset',
        'gather_timeout': 10,
        'filter': 'test_filter',
        'other_arg': 'value'
    }
    task.collections = ['test_collection']
    task.module_defaults = []
    task._parent._play._action_groups = {}

    connection = MagicMock()
    connection._load_name = 'local'

    display = MagicMock()

    shared_loader_obj = MagicMock()
    shared_loader_obj.module_loader.find_plugin_with_context.return_value.resolved_fqcn = 'test_fqcn'

    templar = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()

    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    return action_module

def test_get_module_args(action_module):
    fact_module = 'test_module'
    task_vars = {}

    with patch('ansible.plugins.action.gather_facts.get_action_args_with_defaults', wraps=get_action_args_with_defaults) as mock_get_action_args_with_defaults:
        mod_args = action_module._get_module_args(fact_module, task_vars)

        assert 'gather_subset' not in mod_args
        assert 'gather_timeout' not in mod_args
        assert 'filter' not in mod_args
        assert 'other_arg' in mod_args
        assert mod_args['other_arg'] == 'value'

        mock_get_action_args_with_defaults.assert_called_once_with(
            'test_fqcn', {'other_arg': 'value'}, [], action_module._templar,
            action_groups={}
        )

def test_get_module_args_with_network_connection(action_module):
    action_module._connection._load_name = 'network_cli'
    fact_module = 'test_module'
    task_vars = {}

    with patch('ansible.plugins.action.gather_facts.get_action_args_with_defaults', wraps=get_action_args_with_defaults) as mock_get_action_args_with_defaults:
        mod_args = action_module._get_module_args(fact_module, task_vars)

        assert 'gather_subset' in mod_args
        assert 'gather_timeout' not in mod_args
        assert 'filter' not in mod_args
        assert 'other_arg' in mod_args
        assert mod_args['other_arg'] == 'value'

        mock_get_action_args_with_defaults.assert_called_once_with(
            'test_fqcn', {'gather_subset': 'test_subset', 'other_arg': 'value'}, [], action_module._templar,
            action_groups={}
        )

def test_get_module_args_with_action_setup(action_module):
    with patch('ansible.constants._ACTION_SETUP', new=['test_module']):
        fact_module = 'test_module'
        task_vars = {}

        with patch('ansible.plugins.action.gather_facts.get_action_args_with_defaults', wraps=get_action_args_with_defaults) as mock_get_action_args_with_defaults:
            mod_args = action_module._get_module_args(fact_module, task_vars)

            assert 'gather_subset' in mod_args
            assert 'gather_timeout' in mod_args
            assert 'filter' in mod_args
            assert 'other_arg' in mod_args
            assert mod_args['other_arg'] == 'value'

            mock_get_action_args_with_defaults.assert_called_once_with(
                'test_fqcn', {
                    'gather_subset': 'test_subset',
                    'gather_timeout': 10,
                    'filter': 'test_filter',
                    'other_arg': 'value'
                }, [], action_module._templar,
                action_groups={}
            )
