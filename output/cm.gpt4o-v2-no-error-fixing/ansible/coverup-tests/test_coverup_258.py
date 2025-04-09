# file: lib/ansible/playbook/play.py:328-335
# asked: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}
# gained: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}

import pytest
from ansible.playbook.play import Play
from ansible.playbook.block import Block

class MockTask:
    def __init__(self, name):
        self.name = name

def test_get_tasks_with_blocks(monkeypatch):
    # Mocking pre_tasks, tasks, and post_tasks
    block = Block()
    block.block = [MockTask('block_task')]
    block.rescue = [MockTask('rescue_task')]
    block.always = [MockTask('always_task')]

    play = Play()
    monkeypatch.setattr(play, 'pre_tasks', [block])
    monkeypatch.setattr(play, 'tasks', [])
    monkeypatch.setattr(play, 'post_tasks', [])

    tasklist = play.get_tasks()
    assert len(tasklist) == 1
    assert len(tasklist[0]) == 3
    assert tasklist[0][0].name == 'block_task'
    assert tasklist[0][1].name == 'rescue_task'
    assert tasklist[0][2].name == 'always_task'

def test_get_tasks_without_blocks(monkeypatch):
    # Mocking pre_tasks, tasks, and post_tasks
    task = MockTask('regular_task')

    play = Play()
    monkeypatch.setattr(play, 'pre_tasks', [task])
    monkeypatch.setattr(play, 'tasks', [])
    monkeypatch.setattr(play, 'post_tasks', [])

    tasklist = play.get_tasks()
    assert len(tasklist) == 1
    assert tasklist[0].name == 'regular_task'
