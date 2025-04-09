# file: lib/ansible/plugins/callback/junit.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_play_start(callback_module):
    play_mock = Mock()
    play_mock.get_name.return_value = "test_play"
    
    callback_module.v2_playbook_on_play_start(play_mock)
    
    assert callback_module._play_name == "test_play"
