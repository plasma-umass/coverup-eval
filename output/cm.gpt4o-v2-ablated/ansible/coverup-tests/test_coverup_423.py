# file: lib/ansible/plugins/callback/default.py:232-245
# asked: {"lines": [233, 234, 235, 237, 238, 239, 241, 243, 245], "branches": [[234, 235], [234, 237], [238, 239], [238, 241]]}
# gained: {"lines": [233, 234, 235, 237, 238, 239, 241, 243, 245], "branches": [[234, 235], [234, 237], [238, 239], [238, 241]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def play():
    return MagicMock()

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_play_start_with_name_and_check_mode(callback_module, play):
    play.get_name.return_value = "Test Play"
    play.check_mode = True
    callback_module.check_mode_markers = True

    with patch.object(callback_module._display, 'banner') as mock_banner:
        callback_module.v2_playbook_on_play_start(play)
        mock_banner.assert_called_once_with(u"PLAY [Test Play] [CHECK MODE]")
        assert callback_module._play == play

def test_v2_playbook_on_play_start_with_name_no_check_mode(callback_module, play):
    play.get_name.return_value = "Test Play"
    play.check_mode = False
    callback_module.check_mode_markers = True

    with patch.object(callback_module._display, 'banner') as mock_banner:
        callback_module.v2_playbook_on_play_start(play)
        mock_banner.assert_called_once_with(u"PLAY [Test Play]")
        assert callback_module._play == play

def test_v2_playbook_on_play_start_no_name_with_check_mode(callback_module, play):
    play.get_name.return_value = ""
    play.check_mode = True
    callback_module.check_mode_markers = True

    with patch.object(callback_module._display, 'banner') as mock_banner:
        callback_module.v2_playbook_on_play_start(play)
        mock_banner.assert_called_once_with(u"PLAY [CHECK MODE]")
        assert callback_module._play == play

def test_v2_playbook_on_play_start_no_name_no_check_mode(callback_module, play):
    play.get_name.return_value = ""
    play.check_mode = False
    callback_module.check_mode_markers = True

    with patch.object(callback_module._display, 'banner') as mock_banner:
        callback_module.v2_playbook_on_play_start(play)
        mock_banner.assert_called_once_with(u"PLAY")
        assert callback_module._play == play
