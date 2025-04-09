# file: lib/ansible/playbook/play.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312, 313], "branches": []}

import pytest
from ansible.playbook.play import Play

def test_get_vars():
    play = Play()
    play.vars = {'key': 'value'}
    vars_copy = play.get_vars()
    
    assert vars_copy == {'key': 'value'}
    assert vars_copy is not play.vars  # Ensure it's a copy, not the same object
