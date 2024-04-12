# file lib/ansible/executor/play_iterator.py:560-561
# lines [561]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.task import Task
from ansible.inventory.host import Host
from unittest.mock import MagicMock

# Mocking the necessary parts to test the PlayIterator.add_tasks method
class FakeHostState:
    def __init__(self, tasks):
        self.tasks = tasks

class TestPlayIterator:
    @pytest.fixture
    def play_iterator(self, mocker):
        mocker.patch('ansible.executor.play_iterator.PlayIterator._insert_tasks_into_state', return_value=FakeHostState([]))
        inventory = mocker.MagicMock()
        play = mocker.MagicMock()
        play_context = mocker.MagicMock()
        variable_manager = mocker.MagicMock()
        all_vars = mocker.MagicMock()
        return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

    @pytest.fixture
    def host(self):
        return Host(name='testhost')

    def test_add_tasks(self, play_iterator, host):
        # Given a list of tasks
        task_list = [Task(), Task()]

        # When adding tasks to the host
        play_iterator.add_tasks(host, task_list)

        # Then the host state should be updated with the new tasks
        assert host.name in play_iterator._host_states
        assert isinstance(play_iterator._host_states[host.name], FakeHostState)
        assert play_iterator._host_states[host.name].tasks == []

        # Cleanup is handled by pytest fixtures
