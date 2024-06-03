# file lib/ansible/plugins/action/copy.py:204-207
# lines [204, 206]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def mock_action_base(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)
    return mocker

def test_action_module_transfers_files(mock_action_base):
    action_module = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())
    assert action_module.TRANSFERS_FILES is True
