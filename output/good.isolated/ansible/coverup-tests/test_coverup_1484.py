# file lib/ansible/playbook/play_context.py:167-168
# lines [168]
# branches []

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.playbook.play import Play

@pytest.fixture
def mock_play(mocker):
    play = mocker.MagicMock(spec=Play)
    play.force_handlers = True
    return play

def test_set_attributes_from_play_force_handlers(mock_play):
    play_context = PlayContext()
    # Precondition: attribute should not be set, or should be set to its default value
    assert not hasattr(play_context, 'force_handlers') or play_context.force_handlers is False

    play_context.set_attributes_from_play(mock_play)

    # Postcondition: attribute should be set to True
    assert play_context.force_handlers is True
