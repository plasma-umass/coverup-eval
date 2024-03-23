# file lib/ansible/plugins/callback/default.py:232-245
# lines [233, 234, 235, 237, 238, 239, 241, 243, 245]
# branches ['234->235', '234->237', '238->239', '238->241']

import pytest
from ansible.plugins.callback import default
from ansible.playbook.play import Play

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display')

@pytest.fixture
def callback_module(mock_display):
    callback = default.CallbackModule()
    callback._display = mock_display
    return callback

def test_v2_playbook_on_play_start_with_check_mode_and_name(callback_module, mocker):
    mock_play = mocker.Mock(spec=Play)
    mock_play.get_name.return_value = "test_play"
    mock_play.check_mode = True
    callback_module.check_mode_markers = True

    callback_module.v2_playbook_on_play_start(mock_play)

    mock_play.get_name.assert_called_once()
    callback_module._display.banner.assert_called_once_with(u"PLAY [test_play] [CHECK MODE]")

def test_v2_playbook_on_play_start_without_check_mode_and_name(callback_module, mocker):
    mock_play = mocker.Mock(spec=Play)
    mock_play.get_name.return_value = "test_play"
    mock_play.check_mode = False
    callback_module.check_mode_markers = False

    callback_module.v2_playbook_on_play_start(mock_play)

    mock_play.get_name.assert_called_once()
    callback_module._display.banner.assert_called_once_with(u"PLAY [test_play]")

def test_v2_playbook_on_play_start_with_check_mode_and_no_name(callback_module, mocker):
    mock_play = mocker.Mock(spec=Play)
    mock_play.get_name.return_value = " "
    mock_play.check_mode = True
    callback_module.check_mode_markers = True

    callback_module.v2_playbook_on_play_start(mock_play)

    mock_play.get_name.assert_called_once()
    callback_module._display.banner.assert_called_once_with(u"PLAY [CHECK MODE]")

def test_v2_playbook_on_play_start_without_check_mode_and_no_name(callback_module, mocker):
    mock_play = mocker.Mock(spec=Play)
    mock_play.get_name.return_value = " "
    mock_play.check_mode = False
    callback_module.check_mode_markers = False

    callback_module.v2_playbook_on_play_start(mock_play)

    mock_play.get_name.assert_called_once()
    callback_module._display.banner.assert_called_once_with(u"PLAY")
