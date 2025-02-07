# file: lib/ansible/playbook/helpers.py:33-81
# asked: {"lines": [44], "branches": [[43, 44], [47, 81]]}
# gained: {"lines": [44], "branches": [[43, 44], [47, 81]]}

import pytest
from ansible.playbook.helpers import load_list_of_blocks
from ansible.errors import AnsibleAssertionError

def test_load_list_of_blocks_with_invalid_ds():
    with pytest.raises(AnsibleAssertionError, match="should be a list or None but is"):
        load_list_of_blocks("invalid_ds", play=None)

def test_load_list_of_blocks_with_empty_list():
    result = load_list_of_blocks([], play=None)
    assert result == []

def test_load_list_of_blocks_with_valid_ds(mocker):
    mock_block = mocker.patch('ansible.playbook.block.Block')
    mock_block.is_block.side_effect = [False, True]
    mock_block.load.return_value = "mock_block"

    ds = [{'task': 'task1'}, {'block': 'block1'}]
    result = load_list_of_blocks(ds, play=None)

    assert result == ["mock_block", "mock_block"]
    mock_block.is_block.assert_called()
    mock_block.load.assert_called()

