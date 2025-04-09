# file: lib/ansible/plugins/callback/junit.py:276-278
# asked: {"lines": [276, 277, 278], "branches": []}
# gained: {"lines": [276, 277, 278], "branches": []}

import os
import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def playbook_mock():
    playbook = Mock()
    playbook._file_name = "/path/to/playbook.yml"
    return playbook

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_start(callback_module, playbook_mock):
    callback_module.v2_playbook_on_start(playbook_mock)
    assert callback_module._playbook_path == "/path/to/playbook.yml"
    assert callback_module._playbook_name == "playbook"
