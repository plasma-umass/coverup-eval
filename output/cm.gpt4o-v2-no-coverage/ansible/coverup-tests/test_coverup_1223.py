# file: lib/ansible/executor/play_iterator.py:230-234
# asked: {"lines": [234], "branches": []}
# gained: {"lines": [234], "branches": []}

import pytest
from ansible.executor.play_iterator import PlayIterator
from ansible.playbook.block import Block
from ansible.playbook.task import Task

@pytest.fixture
def play_iterator(mocker):
    mock_play = mocker.Mock()
    mock_play.gather_subset = None
    mock_play.gather_timeout = None
    mock_play.fact_path = None
    mock_play.tags = None
    mock_play._loader = None
    mock_play._included_conditional = None
    mock_play.compile.return_value = []
    mock_play.only_tags = set()
    mock_play.skip_tags = set()
    mock_inventory = mocker.Mock()
    mock_inventory.get_hosts.return_value = []
    mock_play_context = mocker.Mock()
    mock_variable_manager = mocker.Mock()
    mock_all_vars = {}
    return PlayIterator(mock_inventory, mock_play, mock_play_context, mock_variable_manager, mock_all_vars)

def test_cache_block_tasks(play_iterator):
    block = Block()
    result = play_iterator.cache_block_tasks(block)
    assert result is None
