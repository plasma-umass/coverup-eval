# file lib/ansible/plugins/callback/junit.py:307-308
# lines [308]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_include(callback_module, mocker):
    included_file = MagicMock()
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_playbook_on_include(included_file)

    mock_finish_task.assert_called_once_with('included', included_file)
