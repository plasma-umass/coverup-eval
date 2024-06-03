# file lib/ansible/plugins/strategy/free.py:67-69
# lines [67, 68, 69]
# branches []

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def mock_tqm():
    return Mock()

def test_strategy_module_initialization(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned == False
    assert strategy._tqm == mock_tqm

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
