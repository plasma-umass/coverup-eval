# file lib/ansible/playbook/play.py:328-335
# lines [328, 329, 330, 331, 332, 334, 335]
# branches ['330->331', '330->335', '331->332', '331->334']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.play import Play

# Mock classes to represent tasks and blocks
class MockTask:
    pass

class MockBlock(Block):
    def __init__(self):
        self.block = [MockTask()]
        self.rescue = [MockTask()]
        self.always = [MockTask()]

@pytest.fixture
def mock_play():
    play = Play()
    play.pre_tasks = [MockTask()]
    play.tasks = [MockBlock()]
    play.post_tasks = [MockTask()]
    return play

def test_get_tasks_with_block(mock_play):
    tasks = mock_play.get_tasks()
    assert len(tasks) == 3  # pre_tasks + tasks + post_tasks
    assert isinstance(tasks[0], MockTask)
    assert isinstance(tasks[1], list)  # This is the block, which is a list of tasks
    assert len(tasks[1]) == 3  # block + rescue + always
    assert all(isinstance(task, MockTask) for task in tasks[1])  # All tasks in the block are MockTask
    assert isinstance(tasks[2], MockTask)
