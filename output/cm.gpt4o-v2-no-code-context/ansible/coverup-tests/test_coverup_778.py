# file: lib/ansible/plugins/callback/junit.py:307-308
# asked: {"lines": [307, 308], "branches": []}
# gained: {"lines": [307, 308], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.plugins.callback import CallbackBase

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_include(callback_module, mocker):
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')
    included_file = 'test_included_file.yml'
    
    callback_module.v2_playbook_on_include(included_file)
    
    mock_finish_task.assert_called_once_with('included', included_file)
