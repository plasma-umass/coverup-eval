# file: lib/ansible/playbook/task.py:256-264
# asked: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}
# gained: {"lines": [257, 258, 259, 261, 264], "branches": [[257, 258], [257, 264]]}

import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError
from unittest.mock import MagicMock

def test_load_loop_control_with_non_dict():
    task = Task()
    non_dict_input = "not_a_dict"
    
    with pytest.raises(AnsibleParserError) as excinfo:
        task._load_loop_control('loop_control', non_dict_input)
    
    assert "the `loop_control` value must be specified as a dictionary" in str(excinfo.value)

def test_load_loop_control_with_dict(monkeypatch):
    task = Task()
    dict_input = {"key": "value"}
    
    mock_loop_control = MagicMock()
    monkeypatch.setattr('ansible.playbook.task.LoopControl.load', mock_loop_control)
    
    task._variable_manager = MagicMock()
    task._loader = MagicMock()
    
    task._load_loop_control('loop_control', dict_input)
    
    mock_loop_control.assert_called_once_with(data=dict_input, variable_manager=task._variable_manager, loader=task._loader)
