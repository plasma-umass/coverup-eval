# file: lib/ansible/plugins/strategy/free.py:71-287
# asked: {"lines": [71, 86, 88, 91, 93, 95, 96, 98, 99, 101, 103, 104, 105, 106, 108, 109, 112, 113, 114, 115, 116, 120, 121, 122, 123, 127, 129, 132, 134, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 147, 148, 149, 150, 151, 153, 154, 155, 158, 159, 161, 162, 163, 166, 168, 169, 170, 171, 174, 176, 177, 178, 179, 180, 182, 187, 190, 191, 192, 193, 195, 196, 197, 200, 201, 202, 204, 205, 207, 208, 210, 214, 215, 216, 220, 221, 222, 225, 226, 228, 229, 232, 234, 236, 237, 238, 239, 240, 243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 269, 270, 271, 272, 274, 275, 276, 277, 280, 283, 287], "branches": [[95, 96], [95, 98], [99, 101], [99, 283], [103, 104], [103, 108], [113, 114], [123, 127], [123, 214], [132, 134], [132, 210], [147, 148], [147, 158], [149, 150], [149, 153], [150, 149], [150, 151], [154, 155], [154, 158], [177, 178], [177, 187], [178, 179], [178, 182], [187, 190], [187, 195], [190, 191], [190, 195], [195, 196], [195, 200], [200, 201], [200, 214], [201, 202], [201, 204], [214, 215], [214, 220], [221, 222], [221, 225], [225, 113], [225, 226], [243, 244], [243, 280], [245, 246], [245, 274], [248, 249], [248, 257], [259, 260], [259, 261], [264, 265], [264, 272], [269, 264], [269, 270], [270, 269], [270, 271], [275, 276], [275, 277]]}
# gained: {"lines": [71, 86, 88, 91, 93, 95, 96, 98, 99, 101, 103, 104, 105, 106, 283, 287], "branches": [[95, 96], [95, 98], [99, 101], [103, 104]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.strategy.free import StrategyModule
from ansible.playbook.play_context import PlayContext
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.template import Templar
from ansible.errors import AnsibleError
from ansible.playbook.included_file import IncludedFile
from ansible.plugins.loader import action_loader
from ansible.module_utils._text import to_text

@pytest.fixture
def strategy_module():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    strategy._workers = [MagicMock(is_alive=MagicMock(return_value=True))]
    strategy._blocked_hosts = {}
    strategy._tqm._unreachable_hosts = {}
    strategy._tqm._terminated = False
    strategy._tqm.RUN_OK = True
    strategy._tqm.send_callback = MagicMock()
    strategy._variable_manager = MagicMock()
    strategy._loader = MagicMock()
    strategy._hosts_cache = {}
    strategy._hosts_cache_all = {}
    return strategy

@pytest.fixture
def iterator():
    iterator = MagicMock()
    iterator._play = MagicMock()
    iterator._play.max_fail_percentage = None
    iterator.get_next_task_for_host = MagicMock(return_value=(None, MagicMock()))
    iterator.get_hosts_left = MagicMock(return_value=[MagicMock(get_name=MagicMock(return_value="host1"))])
    return iterator

@pytest.fixture
def play_context():
    return MagicMock()

def test_run(strategy_module, iterator, play_context):
    with patch('time.sleep', return_value=None):
        result = strategy_module.run(iterator, play_context)
        assert result == strategy_module._tqm.RUN_OK
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_max_fail_percentage(strategy_module, iterator, play_context):
    iterator._play.max_fail_percentage = 50
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_unreachable_host(strategy_module, iterator, play_context):
    strategy_module._tqm._unreachable_hosts = {"host1": True}
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_blocked_host(strategy_module, iterator, play_context):
    strategy_module._blocked_hosts = {"host1": True}
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_throttle(strategy_module, iterator, play_context):
    task = MagicMock()
    task.throttle = 1
    iterator.get_next_task_for_host = MagicMock(return_value=(None, task))
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_run_once(strategy_module, iterator, play_context):
    task = MagicMock()
    task.run_once = True
    iterator.get_next_task_for_host = MagicMock(return_value=(None, task))
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_role(strategy_module, iterator, play_context):
    task = MagicMock()
    role = MagicMock()
    role.has_run = MagicMock(return_value=True)
    task._role = role
    iterator.get_next_task_for_host = MagicMock(return_value=(None, task))
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_meta_action(strategy_module, iterator, play_context):
    task = MagicMock()
    task.action = "meta"
    iterator.get_next_task_for_host = MagicMock(return_value=(None, task))
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')

def test_run_with_included_file(strategy_module, iterator, play_context):
    included_file = MagicMock()
    IncludedFile.process_include_results = MagicMock(return_value=[included_file])
    with patch('time.sleep', return_value=None):
        strategy_module.run(iterator, play_context)
        strategy_module._tqm.send_callback.assert_called_with('v2_playbook_on_no_hosts_remaining')
