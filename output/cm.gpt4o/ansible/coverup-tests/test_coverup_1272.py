# file lib/ansible/plugins/callback/junit.py:276-278
# lines [277, 278]
# branches []

import os
import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_playbook():
    playbook = Mock()
    playbook._file_name = '/path/to/playbook.yml'
    return playbook

def test_v2_playbook_on_start(mock_playbook):
    callback = CallbackModule()
    callback.v2_playbook_on_start(mock_playbook)
    
    assert callback._playbook_path == '/path/to/playbook.yml'
    assert callback._playbook_name == 'playbook'
