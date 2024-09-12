# file: lib/ansible/playbook/loop_control.py:26-40
# asked: {"lines": [26, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 40], "branches": []}
# gained: {"lines": [26, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 40], "branches": []}

import pytest
from ansible.playbook.loop_control import LoopControl
from ansible.playbook.attribute import FieldAttribute
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def loop_control():
    return LoopControl()

def test_loop_control_initialization(loop_control):
    assert isinstance(loop_control, LoopControl)
    assert loop_control._loop_var.default == 'item'
    assert loop_control._pause.default == 0.0

def test_loop_control_load_method(loop_control, mocker):
    mock_load_data = mocker.patch.object(FieldAttributeBase, 'load_data', return_value='loaded_data')
    data = {'some': 'data'}
    result = LoopControl.load(data)
    mock_load_data.assert_called_once_with(data, variable_manager=None, loader=None)
    assert result == 'loaded_data'
