# file lib/ansible/plugins/action/unarchive.py:29-32
# lines [29, 31]
# branches []

import pytest
from unittest.mock import patch
from ansible.plugins.action.unarchive import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_transfers_files(action_module):
    assert action_module.TRANSFERS_FILES is True

@patch('ansible.plugins.action.unarchive.ActionBase')
def test_action_module_initialization(mock_action_base):
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is True
