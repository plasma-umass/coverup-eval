# file lib/ansible/executor/play_iterator.py:145-219
# lines [146, 147, 148, 151, 152, 153, 155, 158, 159, 160, 161, 162, 163, 167, 168, 170, 171, 172, 173, 174, 176, 177, 178, 180, 181, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 209, 210, 211, 213, 217, 219]
# branches ['167->168', '167->170', '170->171', '170->172', '172->173', '172->174', '176->177', '176->178', '183->184', '183->188', '185->183', '185->186', '192->193', '192->213', '196->192', '196->197', '197->198', '199->200', '199->201', '201->203', '201->206', '209->192', '209->210', '213->217', '213->219']

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.playbook.play_context import PlayContext
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.host import Host
from ansible.template import Templar

# Mock classes to simulate the necessary parts of Ansible internals
class MockLoader(DataLoader):
    def get_basedir(self):
        return super(MockLoader, self).get_basedir()

class MockInventory(InventoryManager):
    def get_hosts(self, pattern, order=None):
        return [Host(name='testhost')]

@pytest.fixture
def mock_play_context(mocker):
    play_context = PlayContext()
    play_context.start_at_task = 'Gathering Facts'
    return play_context

@pytest.fixture
def mock_variable_manager(mocker):
    variable_manager = VariableManager()
    variable_manager._templar = Templar(loader=MockLoader())
    return variable_manager

@pytest.fixture
def mock_play(mocker):
    play = Play()
    play.tags = []
    play.gather_subset = ['all']
    play.gather_timeout = 10
    play.fact_path = '/tmp/facts'
    play._included_conditional = None
    play._loader = MockLoader()
    play.compile = lambda: [Block()]
    play.hosts = 'all'
    play.order = 'inventory'
    return play

def test_play_iterator_start_at_task(mock_play_context, mock_variable_manager, mock_play, mocker):
    inventory = MockInventory(loader=MockLoader(), sources='localhost,')
    all_vars = dict(ansible_play_batch=['testhost'], ansible_play_hosts=['testhost'])

    # Create the PlayIterator with the mocked objects
    play_iterator = PlayIterator(
        inventory=inventory,
        play=mock_play,
        play_context=mock_play_context,
        variable_manager=mock_variable_manager,
        all_vars=all_vars,
        start_at_done=False
    )

    # Check if the start_at_task has been cleared, indicating the lines were executed
    assert play_iterator._host_states['testhost'].did_start_at_task is True
    assert play_iterator._host_states['testhost'].run_state == play_iterator.ITERATING_SETUP
    assert mock_play_context.start_at_task is None
