# file: lib/ansible/executor/play_iterator.py:462-468
# asked: {"lines": [462, 463, 464, 465, 466, 467, 468], "branches": []}
# gained: {"lines": [462, 463, 464, 465, 466, 467, 468], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.block import Block
from ansible.playbook.task import Task

@pytest.fixture
def play_iterator():
    play = Mock()
    play.gather_subset = None
    play.gather_timeout = None
    play.fact_path = None
    play.tags = None
    play.only_tags = set()
    play.skip_tags = set()
    play._included_conditional = None
    play._loader = None
    play.compile.return_value = []
    play._removed_hosts = []

    inventory = Mock()
    inventory.get_hosts.return_value = []

    play_context = Mock()
    play_context.start_at_task = None

    variable_manager = Mock()
    all_vars = {}

    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_mark_host_failed(play_iterator):
    host = Mock()
    host.name = "test_host"

    play_iterator._host_states = {host.name: "initial_state"}
    play_iterator.get_host_state = Mock(return_value="initial_state")
    play_iterator._set_failed_state = Mock(return_value="failed_state")

    with patch('ansible.executor.play_iterator.display.debug') as mock_debug:
        play_iterator.mark_host_failed(host)

        play_iterator.get_host_state.assert_called_once_with(host)
        play_iterator._set_failed_state.assert_called_once_with("initial_state")
        assert play_iterator._host_states[host.name] == "failed_state"
        assert host.name in play_iterator._play._removed_hosts

        mock_debug.assert_any_call("marking host %s failed, current state: %s" % (host, "initial_state"))
        mock_debug.assert_any_call("^ failed state is now: %s" % "failed_state")
