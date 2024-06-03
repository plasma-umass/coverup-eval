# file lib/ansible/plugins/strategy/linear.py:50-53
# lines [50, 52]
# branches []

import pytest
from unittest.mock import patch
from ansible.plugins.strategy.linear import StrategyModule

@pytest.fixture
def mock_strategy_base(mocker):
    mocker.patch('ansible.plugins.strategy.linear.StrategyBase.__init__', return_value=None)

def test_strategy_module_noop_task(mock_strategy_base):
    strategy = StrategyModule(tqm=None)
    assert strategy.noop_task is None
