# file lib/ansible/plugins/action/pause.py:298-304
# lines [298, 299, 300, 301, 302, 303, 304]
# branches ['299->300', '301->302', '301->303', '303->299', '303->304']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.action.pause import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def action_module():
    task = Mock(spec=Task)
    connection = Mock()
    play_context = Mock(spec=PlayContext)
    loader = Mock(spec=DataLoader)
    templar = Mock(spec=Templar)
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_c_or_a_c_pressed(action_module):
    stdin_mock = Mock()
    stdin_mock.read = Mock(side_effect=[b'c'])
    
    result = action_module._c_or_a(stdin_mock)
    
    assert result is True

def test_c_or_a_a_pressed(action_module):
    stdin_mock = Mock()
    stdin_mock.read = Mock(side_effect=[b'a'])
    
    result = action_module._c_or_a(stdin_mock)
    
    assert result is False

def test_c_or_a_other_pressed_then_c(action_module):
    stdin_mock = Mock()
    stdin_mock.read = Mock(side_effect=[b'x', b'c'])
    
    result = action_module._c_or_a(stdin_mock)
    
    assert result is True

def test_c_or_a_other_pressed_then_a(action_module):
    stdin_mock = Mock()
    stdin_mock.read = Mock(side_effect=[b'x', b'a'])
    
    result = action_module._c_or_a(stdin_mock)
    
    assert result is False
