# file lib/ansible/playbook/play.py:328-335
# lines [329, 330, 331, 332, 334, 335]
# branches ['330->331', '330->335', '331->332', '331->334']

import pytest
from unittest.mock import Mock, patch

# Assuming the Play class and other dependencies are imported from ansible.playbook.play
from ansible.playbook.play import Play, Block

@pytest.fixture
def play_instance():
    play = Play()
    play.pre_tasks = []
    play.tasks = []
    play.post_tasks = []
    return play

def test_get_tasks_with_block(play_instance):
    block = Mock(spec=Block)
    block.block = ['block_task']
    block.rescue = ['rescue_task']
    block.always = ['always_task']
    
    play_instance.tasks = [block]
    
    tasklist = play_instance.get_tasks()
    
    assert tasklist == [['block_task', 'rescue_task', 'always_task']]

def test_get_tasks_without_block(play_instance):
    task = Mock()
    
    play_instance.tasks = [task]
    
    tasklist = play_instance.get_tasks()
    
    assert tasklist == [task]
