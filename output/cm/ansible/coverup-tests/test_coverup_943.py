# file lib/ansible/plugins/strategy/linear.py:50-53
# lines [50, 52]
# branches []

import pytest
from ansible.plugins.strategy.linear import StrategyModule
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.task import Task
from unittest.mock import MagicMock

# Mocking the StrategyBase class to avoid any side effects
class MockStrategyBase:
    def __init__(self, *args, **kwargs):
        pass

# Replacing the StrategyBase with the mock within the StrategyModule class
StrategyModule.__bases__ = (MockStrategyBase,)

@pytest.fixture
def strategy_module():
    # Setup for the test
    strategy = StrategyModule()
    yield strategy
    # Teardown after the test
    # (No specific teardown required in this case)

def test_noop_task(strategy_module, mocker):
    # Ensure that the noop_task is None initially
    assert strategy_module.noop_task is None

    # Mock the TaskQueueManager to avoid side effects
    mocker.patch.object(TaskQueueManager, '__init__', return_value=None)

    # Mock the Task to avoid side effects
    mocker.patch.object(Task, '__init__', return_value=None)

    # Create a noop task
    strategy_module.noop_task = Task()

    # Assert that the noop_task is no longer None
    assert strategy_module.noop_task is not None
