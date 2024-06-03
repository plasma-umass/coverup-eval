# file lib/ansible/plugins/callback/junit.py:280-281
# lines [280, 281]
# branches []

import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_play():
    return Mock()

def test_v2_playbook_on_play_start(mock_play):
    callback = CallbackModule()
    mock_play.get_name.return_value = "test_play"
    
    callback.v2_playbook_on_play_start(mock_play)
    
    assert callback._play_name == "test_play"
