# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [325, 326], "branches": []}
# gained: {"lines": [325, 326], "branches": []}

import pytest
from ansible.playbook.play import Play

def test_get_roles():
    play = Play()
    play.roles = ['role1', 'role2', 'role3']
    
    roles_copy = play.get_roles()
    
    assert roles_copy == ['role1', 'role2', 'role3']
    assert roles_copy is not play.roles  # Ensure it's a copy, not the same list object
