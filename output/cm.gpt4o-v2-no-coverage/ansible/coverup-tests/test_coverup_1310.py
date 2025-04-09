# file: lib/ansible/executor/play_iterator.py:522-524
# asked: {"lines": [524], "branches": []}
# gained: {"lines": [524], "branches": []}

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.block import Block
from ansible.playbook.task import Task

class MockInventory:
    def get_hosts(self, hosts, order):
        return [MockHost("localhost")]

class MockPlay:
    def __init__(self):
        self.gather_subset = None
        self.gather_timeout = None
        self.fact_path = None
        self.tags = None
        self.only_tags = []
        self.skip_tags = []
        self._loader = None
        self._included_conditional = None
        self.hosts = []
        self.order = None

    def compile(self):
        return []

class MockPlayContext:
    def __init__(self):
        self.start_at_task = None

class MockHost:
    def __init__(self, name):
        self.name = name

class MockTask:
    pass

@pytest.fixture
def play_iterator():
    inventory = MockInventory()
    play = MockPlay()
    play_context = MockPlayContext()
    variable_manager = None
    all_vars = None
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_get_original_task(play_iterator):
    host = MockHost(name="localhost")
    task = MockTask()
    
    original_task = play_iterator.get_original_task(host, task)
    
    assert original_task == (None, None)
