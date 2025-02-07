# file: lib/ansible/plugins/callback/default.py:232-245
# asked: {"lines": [233, 234, 235, 237, 238, 239, 241, 243, 245], "branches": [[234, 235], [234, 237], [238, 239], [238, 241]]}
# gained: {"lines": [233, 234, 235, 237, 238, 239, 241, 243, 245], "branches": [[234, 235], [234, 237], [238, 239], [238, 241]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_play_start_with_name_and_check_mode(callback_module, mocker):
    play = Mock()
    play.get_name.return_value = "Test Play"
    play.check_mode = True
    callback_module.check_mode_markers = True

    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.banner = Mock()

    callback_module.v2_playbook_on_play_start(play)

    assert callback_module._play == play
    mock_display.banner.assert_called_once_with("PLAY [Test Play] [CHECK MODE]")

def test_v2_playbook_on_play_start_with_name_without_check_mode(callback_module, mocker):
    play = Mock()
    play.get_name.return_value = "Test Play"
    play.check_mode = False
    callback_module.check_mode_markers = True

    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.banner = Mock()

    callback_module.v2_playbook_on_play_start(play)

    assert callback_module._play == play
    mock_display.banner.assert_called_once_with("PLAY [Test Play]")

def test_v2_playbook_on_play_start_without_name_and_check_mode(callback_module, mocker):
    play = Mock()
    play.get_name.return_value = ""
    play.check_mode = True
    callback_module.check_mode_markers = True

    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.banner = Mock()

    callback_module.v2_playbook_on_play_start(play)

    assert callback_module._play == play
    mock_display.banner.assert_called_once_with("PLAY [CHECK MODE]")

def test_v2_playbook_on_play_start_without_name_without_check_mode(callback_module, mocker):
    play = Mock()
    play.get_name.return_value = ""
    play.check_mode = False
    callback_module.check_mode_markers = True

    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.banner = Mock()

    callback_module.v2_playbook_on_play_start(play)

    assert callback_module._play == play
    mock_display.banner.assert_called_once_with("PLAY")
