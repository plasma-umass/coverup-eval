# file lib/ansible/playbook/play_context.py:167-168
# lines [168]
# branches []

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.playbook.play import Play

@pytest.fixture
def mock_play(mocker):
    play = mocker.MagicMock(spec=Play)
    play.force_handlers = False
    return play

def test_set_attributes_from_play_force_handlers(mock_play):
    play_context = PlayContext()
    # Assuming default is None or not set, so we don't assert its initial value

    play_context.set_attributes_from_play(mock_play)
    assert play_context.force_handlers == mock_play.force_handlers

    mock_play.force_handlers = True
    play_context.set_attributes_from_play(mock_play)
    assert play_context.force_handlers == mock_play.force_handlers
