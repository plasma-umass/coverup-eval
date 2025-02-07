# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [325, 326], "branches": []}
# gained: {"lines": [325], "branches": []}

import pytest
from ansible.playbook.play import Play

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
    def __init__(self, roles):
        self.roles = roles

    def get_roles(self):
        return self.roles[:]

def test_get_roles():
    roles = ['role1', 'role2', 'role3']
    play = MockPlay(roles)
    result = play.get_roles()
    assert result == roles
    assert result is not roles  # Ensure a copy is returned
