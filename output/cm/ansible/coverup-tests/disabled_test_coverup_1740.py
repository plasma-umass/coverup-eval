# file lib/ansible/executor/play_iterator.py:560-561
# lines [561]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.task import Task
from ansible.inventory.host import Host
from unittest.mock import MagicMock

# Mocking the necessary parts to test the PlayIterator.add_tasks method
class TestPlayIterator:
    @pytest.fixture
    def play_iterator(self, mocker):
        inventory = mocker.MagicMock()
        play = mocker.MagicMock()
        play_context = mocker.MagicMock()
        variable_manager = mocker.MagicMock()
        all_vars = mocker.MagicMock()
        mocker.patch('ansible.executor.play_iterator.PlayIterator._insert_tasks_into_state', return_value='mocked_state')
        mocker.patch('ansible.executor.play_iterator.PlayIterator.get_host_state', return_value='initial_state')
        return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

    @pytest.fixture
    def host(self):
        return Host(name='test_host')

    @pytest.fixture
    def task_list(self):
        return [Task()]

    def test_add_tasks(self, play_iterator, host, task_list):
        # Precondition: Ensure the host state is not already set
        assert host.name not in play_iterator._host_states

        # Execute the method that should hit the missing line
        play_iterator.add_tasks(host, task_list)

        # Postcondition: Ensure the host state is now set
        assert host.name in play_iterator._host_states
        assert play_iterator._host_states[host.name] == 'mocked_state'
