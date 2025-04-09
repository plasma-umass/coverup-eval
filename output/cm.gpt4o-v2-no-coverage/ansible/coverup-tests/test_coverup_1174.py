# file: lib/ansible/vars/reserved.py:31-65
# asked: {"lines": [47, 63], "branches": [[46, 47], [52, 57], [57, 60], [60, 63]]}
# gained: {"lines": [47, 63], "branches": [[46, 47], [60, 63]]}

import pytest
from ansible.playbook import Play
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task import Task
from ansible.vars.reserved import get_reserved_names

@pytest.fixture
def mock_play_attributes(monkeypatch):
    class MockPlay:
        def __init__(self):
            self._attributes = {
                'public_attr': 'value',
                'private_attr': 'value',
                'action': 'value',
                'loop': 'value'
            }
    monkeypatch.setattr(Play, '__init__', MockPlay.__init__)

@pytest.fixture
def mock_block_attributes(monkeypatch):
    class MockBlock:
        def __init__(self):
            self._attributes = {
                'public_attr': 'value',
                'private_attr': 'value'
            }
    monkeypatch.setattr(Block, '__init__', MockBlock.__init__)

@pytest.fixture
def mock_role_attributes(monkeypatch):
    class MockRole:
        def __init__(self):
            self._attributes = {
                'public_attr': 'value',
                'private_attr': 'value'
            }
    monkeypatch.setattr(Role, '__init__', MockRole.__init__)

@pytest.fixture
def mock_task_attributes(monkeypatch):
    class MockTask:
        def __init__(self):
            self._attributes = {
                'public_attr': 'value',
                'private_attr': 'value'
            }
    monkeypatch.setattr(Task, '__init__', MockTask.__init__)

def test_get_reserved_names_include_private(mock_play_attributes, mock_block_attributes, mock_role_attributes, mock_task_attributes):
    reserved_names = get_reserved_names(include_private=True)
    assert 'public_attr' in reserved_names
    assert 'private_attr' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names

def test_get_reserved_names_exclude_private(mock_play_attributes, mock_block_attributes, mock_role_attributes, mock_task_attributes):
    reserved_names = get_reserved_names(include_private=False)
    assert 'public_attr' in reserved_names
    assert 'private_attr' not in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names
