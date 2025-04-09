# file: lib/ansible/plugins/strategy/linear.py:66-72
# asked: {"lines": [66, 67, 68, 69, 70, 72], "branches": []}
# gained: {"lines": [66, 67, 68, 69, 70, 72], "branches": []}

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.errors import AnsibleAssertionError
from ansible.plugins.strategy.linear import StrategyModule

class MockTask:
    pass

class MockTQM:
    def get_inventory(self):
        return None

    def get_variable_manager(self):
        return None

    def get_loader(self):
        return None

    _workers = None
    _final_q = None

@pytest.fixture
def strategy_module():
    tqm = MockTQM()
    strategy = StrategyModule(tqm)
    strategy.noop_task = MockTask()
    return strategy

def test_create_noop_block_from(strategy_module):
    original_block = Block()
    original_block.block = [Task()]
    original_block.always = [Task()]
    original_block.rescue = [Task()]

    parent_block = Block()

    noop_block = strategy_module._create_noop_block_from(original_block, parent_block)

    assert noop_block._parent == parent_block
    assert all(isinstance(task, MockTask) for task in noop_block.block)
    assert all(isinstance(task, MockTask) for task in noop_block.always)
    assert all(isinstance(task, MockTask) for task in noop_block.rescue)

def test_replace_with_noop(strategy_module):
    target = [Task(), Block()]

    with pytest.raises(AnsibleAssertionError):
        strategy_module.noop_task = None
        strategy_module._replace_with_noop(target)

    strategy_module.noop_task = MockTask()
    result = strategy_module._replace_with_noop(target)

    assert len(result) == 2
    assert isinstance(result[0], MockTask)
    assert isinstance(result[1], Block)
    assert all(isinstance(task, MockTask) for task in result[1].block)
    assert all(isinstance(task, MockTask) for task in result[1].always)
    assert all(isinstance(task, MockTask) for task in result[1].rescue)
