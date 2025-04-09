# file lib/ansible/plugins/action/debug.py:33-80
# lines [33, 34, 35, 37, 38, 40, 41, 44, 46, 47, 48, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 64, 66, 68, 70, 73, 75, 76, 78, 80]
# branches ['34->35', '34->37', '37->38', '37->40', '46->47', '46->75', '47->48', '47->50', '50->51', '50->70', '53->55', '53->64', '55->56', '55->58', '61->62', '61->64', '64->66', '64->68']

import pytest
from ansible.plugins.action.debug import ActionModule
from ansible.utils.display import Display
from ansible.template import Templar
from ansible.errors import AnsibleUndefinedVariable, AnsibleActionFail
from ansible.module_utils._text import to_text

# Mock string_types for compatibility with the code snippet provided
string_types = (str,)

@pytest.fixture
def action_debug(mocker):
    mocker.patch('ansible.plugins.action.ActionBase._execute_module')
    action = ActionModule(task=mocker.MagicMock(), connection=mocker.MagicMock(), play_context=mocker.MagicMock(), loader=mocker.MagicMock(), templar=Templar(loader=mocker.MagicMock()), shared_loader_obj=mocker.MagicMock())
    action._display = Display()
    action._task.async_val = False  # Ensure async is not set to avoid AnsibleActionFail
    action._supports_async = True  # Ensure the action supports async to avoid AnsibleActionFail
    return action

def test_action_debug_msg_and_var_incompatible(action_debug):
    action_debug._task.args = {'msg': 'Hello', 'var': 'world'}
    result = action_debug.run(task_vars={})
    assert result['failed']
    assert result['msg'] == "'msg' and 'var' are incompatible options"

def test_action_debug_with_msg(action_debug):
    action_debug._task.args = {'msg': 'Hello'}
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result['msg'] == 'Hello'

def test_action_debug_with_var_as_string(action_debug, mocker):
    action_debug._task.args = {'var': 'my_variable'}
    mocker.patch.object(action_debug._templar, 'template', side_effect=lambda x, **kw: x.strip('{{}}') if '{{' in x else 'templated_value')
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result['my_variable'] == 'templated_value'

def test_action_debug_with_var_as_list(action_debug, mocker):
    action_debug._task.args = {'var': ['my_variable']}
    mocker.patch.object(action_debug._templar, 'template', return_value='templated_value')
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result[to_text(list)] == 'templated_value'

def test_action_debug_with_var_as_dict(action_debug, mocker):
    action_debug._task.args = {'var': {'my_variable': 'value'}}
    mocker.patch.object(action_debug._templar, 'template', return_value='templated_value')
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result[to_text(dict)] == 'templated_value'

def test_action_debug_with_var_undefined(action_debug, mocker):
    action_debug._task.args = {'var': 'undefined_variable'}
    mocker.patch.object(action_debug._templar, 'template', side_effect=AnsibleUndefinedVariable)
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result['undefined_variable'] == "VARIABLE IS NOT DEFINED!"

def test_action_debug_with_high_verbosity(action_debug):
    action_debug._task.args = {'verbosity': 9999}
    action_debug._display.verbosity = 0
    result = action_debug.run(task_vars={})
    assert result['skipped']
    assert result['skipped_reason'] == "Verbosity threshold not met."

def test_action_debug_with_default_msg(action_debug):
    action_debug._task.args = {}
    result = action_debug.run(task_vars={})
    assert not result['failed']
    assert result['msg'] == 'Hello world!'
