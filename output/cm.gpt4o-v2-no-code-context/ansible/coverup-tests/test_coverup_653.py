# file: lib/ansible/plugins/strategy/host_pinned.py:41-45
# asked: {"lines": [41, 43, 44, 45], "branches": []}
# gained: {"lines": [41, 43, 44, 45], "branches": []}

import pytest
from ansible.plugins.strategy import host_pinned
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def mock_tqm(mocker):
    mock_tqm = mocker.Mock(spec=TaskQueueManager)
    mock_tqm._workers = mocker.Mock()  # Mock the _workers attribute
    mock_tqm._final_q = mocker.Mock()  # Mock the _final_q attribute
    return mock_tqm

def test_strategy_module_initialization(mock_tqm):
    strategy_module = host_pinned.StrategyModule(mock_tqm)
    assert strategy_module._host_pinned is True

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here

# Ensure the test runs and covers the lines 41-45
def test_strategy_module_class():
    assert hasattr(host_pinned, 'StrategyModule')
    assert issubclass(host_pinned.StrategyModule, host_pinned.FreeStrategyModule)
