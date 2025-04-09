# file: lib/ansible/playbook/block.py:119-132
# asked: {"lines": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}
# gained: {"lines": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block
from ansible.playbook.helpers import load_list_of_tasks

def test_load_block_success(monkeypatch):
    def mock_load_list_of_tasks(ds, play, block, role, task_include, variable_manager, loader, use_handlers):
        return ["task1", "task2"]

    monkeypatch.setattr("ansible.playbook.block.load_list_of_tasks", mock_load_list_of_tasks)

    block = Block(play="play", role="role", use_handlers=True)
    block._variable_manager = None
    block._loader = None
    result = block._load_block("attr", ["task_ds"])
    assert result == ["task1", "task2"]

def test_load_block_assertion_error(monkeypatch):
    def mock_load_list_of_tasks(ds, play, block, role, task_include, variable_manager, loader, use_handlers):
        raise AssertionError("Test assertion error")

    monkeypatch.setattr("ansible.playbook.block.load_list_of_tasks", mock_load_list_of_tasks)

    block = Block(play="play", role="role", use_handlers=True)
    block._variable_manager = None
    block._loader = None
    block._ds = "dummy_ds"
    with pytest.raises(AnsibleParserError) as excinfo:
        block._load_block("attr", ["task_ds"])
    assert "A malformed block was encountered while loading a block" in str(excinfo.value)
