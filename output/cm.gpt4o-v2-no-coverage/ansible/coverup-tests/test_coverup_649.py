# file: lib/ansible/executor/play_iterator.py:221-228
# asked: {"lines": [221, 225, 226, 228], "branches": [[225, 226], [225, 228]]}
# gained: {"lines": [221, 225, 226, 228], "branches": [[225, 226], [225, 228]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.block import Block
from ansible.playbook.task import Task

class MockHost:
    def __init__(self, name):
        self.name = name

class MockInventory:
    def get_hosts(self, hosts, order):
        return [MockHost(name) for name in hosts]

class MockPlay:
    def __init__(self):
        self.gather_subset = None
        self.gather_timeout = None
        self.fact_path = None
        self.tags = None
        self._loader = None
        self._included_conditional = None
        self.hosts = ['host1', 'host2']
        self.order = 'sorted'
        self.only_tags = None
        self.skip_tags = None

    def compile(self):
        return [Block()]

class MockPlayContext:
    def __init__(self):
        self.start_at_task = None

class MockVariableManager:
    pass

@pytest.fixture
def play_iterator():
    inventory = MockInventory()
    play = MockPlay()
    play_context = MockPlayContext()
    variable_manager = MockVariableManager()
    all_vars = {}
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_get_host_state_creates_stub_state(play_iterator):
    host = MockHost('new_host')
    assert 'new_host' not in play_iterator._host_states
    state = play_iterator.get_host_state(host)
    assert 'new_host' in play_iterator._host_states
    assert play_iterator._host_states['new_host'].copy() == state

def test_get_host_state_returns_existing_state(play_iterator):
    host = MockHost('host1')
    existing_state = play_iterator._host_states[host.name]
    state = play_iterator.get_host_state(host)
    assert state == existing_state.copy()
