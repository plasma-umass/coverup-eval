# file: lib/ansible/playbook/play.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312, 313], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    return Play()

def test_get_vars(play_instance):
    # Setup
    play_instance.vars = {'key': 'value'}
    
    # Execute
    result = play_instance.get_vars()
    
    # Verify
    assert result == {'key': 'value'}
    assert result is not play_instance.vars  # Ensure a copy is returned

    # Cleanup
    play_instance.vars.clear()
