# file lib/ansible/playbook/play.py:328-335
# lines [329, 330, 331, 332, 334, 335]
# branches ['330->331', '330->335', '331->332', '331->334']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.block import Block

# Assuming the existence of a minimal setup for the Play class
# and that the Play class is part of a larger module that we can import.

@pytest.fixture
def mock_block(mocker):
    block = mocker.MagicMock(spec=Block)
    block.block = ['block_task']
    block.rescue = ['rescue_task']
    block.always = ['always_task']
    return block

def test_get_tasks_with_block(mock_block):
    play = Play()
    play.pre_tasks = [mock_block]
    play.tasks = ['normal_task']
    play.post_tasks = []

    expected_tasklist = ['block_task', 'rescue_task', 'always_task', 'normal_task']
    tasklist = play.get_tasks()

    # Flatten the list of tasks since block tasks are appended as a list
    flattened_tasklist = [item for sublist in tasklist for item in (sublist if isinstance(sublist, list) else [sublist])]

    assert flattened_tasklist == expected_tasklist, "Task list did not include block, rescue, and always tasks"
