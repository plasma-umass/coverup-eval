# file lib/ansible/playbook/play.py:280-310
# lines [280, 290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310]
# branches ['297->298', '297->300']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Mock classes to avoid side effects
class MockVariableManager(VariableManager):
    pass

class MockDataLoader(DataLoader):
    pass

class MockRole:
    def __init__(self):
        self.from_include = False

    def compile(self, play=None):
        return [Task()]

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock(spec=MockVariableManager)

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock(spec=MockDataLoader)

@pytest.fixture
def mock_play(mock_variable_manager, mock_loader):
    play = Play()
    play._variable_manager = mock_variable_manager
    play._loader = mock_loader
    play.pre_tasks = [Task()]
    play.tasks = [Task()]
    play.post_tasks = [Task()]
    play.roles = [MockRole()]
    return play

def test_play_compile(mock_play):
    block_list = mock_play.compile()

    # Assertions to check if the block_list contains the correct number of blocks
    assert len(block_list) == 7  # pre_tasks + 3 flush_blocks + _compile_roles + tasks + post_tasks
    assert isinstance(block_list[0], Task)
    assert isinstance(block_list[1], Block)
    assert isinstance(block_list[2], Task)  # This comes from the _compile_roles
    assert isinstance(block_list[3], Task)
    assert isinstance(block_list[4], Block)
    assert isinstance(block_list[5], Task)
    assert isinstance(block_list[6], Block)

    # Check if the flush_blocks have the implicit attribute set to True
    for block in block_list:
        if isinstance(block, Block):
            for task in block.block:
                assert task.implicit is True
