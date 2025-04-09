# file lib/ansible/plugins/callback/junit.py:280-281
# lines [280, 281]
# branches []

import pytest
from ansible.plugins.callback import junit
from ansible.playbook.play import Play

@pytest.fixture
def callback_module():
    return junit.CallbackModule()

def test_v2_playbook_on_play_start(callback_module, mocker):
    mock_play = mocker.MagicMock(spec=Play)
    mock_play.get_name.return_value = "test_play"

    callback_module.v2_playbook_on_play_start(mock_play)

    assert callback_module._play_name == "test_play"
