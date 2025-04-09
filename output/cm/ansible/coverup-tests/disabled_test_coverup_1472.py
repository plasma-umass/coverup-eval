# file lib/ansible/playbook/play.py:312-313
# lines [313]
# branches []

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    # Setup the Play instance
    play = Play()
    play.vars = {'key1': 'value1', 'key2': 'value2'}
    return play

def test_play_get_vars(play_instance):
    # Call the get_vars method
    result_vars = play_instance.get_vars()

    # Assert that the result is a copy of the vars, not the same object
    assert result_vars == play_instance.vars
    assert result_vars is not play_instance.vars
