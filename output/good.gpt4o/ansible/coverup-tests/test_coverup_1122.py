# file lib/ansible/plugins/callback/default.py:232-245
# lines [233, 234, 235, 237, 238, 239, 241, 243, 245]
# branches ['234->235', '234->237', '238->239', '238->241']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def play():
    play = MagicMock()
    play.get_name.return_value = "Test Play"
    play.check_mode = False
    return play

@pytest.fixture
def play_check_mode():
    play = MagicMock()
    play.get_name.return_value = "Test Play"
    play.check_mode = True
    return play

@pytest.fixture
def play_no_name():
    play = MagicMock()
    play.get_name.return_value = ""
    play.check_mode = False
    return play

@pytest.fixture
def play_no_name_check_mode():
    play = MagicMock()
    play.get_name.return_value = ""
    play.check_mode = True
    return play

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_play_start_normal_mode(callback_module, play):
    callback_module.check_mode_markers = True
    callback_module._display = MagicMock()
    callback_module.v2_playbook_on_play_start(play)
    callback_module._display.banner.assert_called_once_with("PLAY [Test Play]")

def test_v2_playbook_on_play_start_check_mode(callback_module, play_check_mode):
    callback_module.check_mode_markers = True
    callback_module._display = MagicMock()
    callback_module.v2_playbook_on_play_start(play_check_mode)
    callback_module._display.banner.assert_called_once_with("PLAY [Test Play] [CHECK MODE]")

def test_v2_playbook_on_play_start_no_name(callback_module, play_no_name):
    callback_module.check_mode_markers = True
    callback_module._display = MagicMock()
    callback_module.v2_playbook_on_play_start(play_no_name)
    callback_module._display.banner.assert_called_once_with("PLAY")

def test_v2_playbook_on_play_start_no_name_check_mode(callback_module, play_no_name_check_mode):
    callback_module.check_mode_markers = True
    callback_module._display = MagicMock()
    callback_module.v2_playbook_on_play_start(play_no_name_check_mode)
    callback_module._display.banner.assert_called_once_with("PLAY [CHECK MODE]")
