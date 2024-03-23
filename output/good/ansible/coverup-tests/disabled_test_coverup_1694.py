# file lib/ansible/plugins/strategy/linear.py:74-81
# lines [75, 76, 77, 78, 79, 81]
# branches []

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.playbook.play_context import PlayContext
from ansible.playbook.play import Play
from ansible.plugins.strategy.linear import StrategyModule

@pytest.fixture
def strategy_module(mocker):
    mocker.patch('ansible.plugins.strategy.StrategyBase.__init__', return_value=None)
    strategy = StrategyModule()
    strategy._tqm = mocker.MagicMock()
    return strategy

@pytest.fixture
def play():
    return Play()

@pytest.fixture
def templar(play):
    return Templar(loader=play.get_loader())

@pytest.fixture
def play_context():
    return PlayContext()

@pytest.fixture
def iterator(play, play_context):
    # Mocking PlayIterator since the original import was incorrect
    class MockPlayIterator:
        def __init__(self, play):
            self._play = play

    return MockPlayIterator(play=play)

def test_prepare_and_create_noop_block_from(strategy_module, iterator):
    # The Block class does not accept 'parent' as an argument, so we remove it
    original_block = Block()

    noop_block = strategy_module._prepare_and_create_noop_block_from(original_block, None, iterator)

    assert isinstance(noop_block, Block)
    assert strategy_module.noop_task.action == 'meta'
    assert strategy_module.noop_task.args['_raw_params'] == 'noop'
    assert strategy_module.noop_task.implicit is True
    assert strategy_module.noop_task._loader == iterator._play._loader
