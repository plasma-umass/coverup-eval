# file: lib/ansible/playbook/play.py:328-335
# asked: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}
# gained: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}

import pytest
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def play_instance():
    return Play()

@pytest.fixture
def block_instance():
    return Block()

def test_get_tasks_with_no_tasks(play_instance):
    play_instance.pre_tasks = []
    play_instance.tasks = []
    play_instance.post_tasks = []
    assert play_instance.get_tasks() == []

def test_get_tasks_with_regular_tasks(play_instance):
    task1 = "task1"
    task2 = "task2"
    play_instance.pre_tasks = [task1]
    play_instance.tasks = [task2]
    play_instance.post_tasks = []
    assert play_instance.get_tasks() == [task1, task2]

def test_get_tasks_with_block_tasks(play_instance, block_instance):
    block_instance.block = ["block_task"]
    block_instance.rescue = ["rescue_task"]
    block_instance.always = ["always_task"]
    play_instance.pre_tasks = [block_instance]
    play_instance.tasks = []
    play_instance.post_tasks = []
    assert play_instance.get_tasks() == [["block_task", "rescue_task", "always_task"]]

def test_get_tasks_with_mixed_tasks(play_instance, block_instance):
    task1 = "task1"
    block_instance.block = ["block_task"]
    block_instance.rescue = ["rescue_task"]
    block_instance.always = ["always_task"]
    play_instance.pre_tasks = [task1]
    play_instance.tasks = [block_instance]
    play_instance.post_tasks = []
    assert play_instance.get_tasks() == [task1, ["block_task", "rescue_task", "always_task"]]
