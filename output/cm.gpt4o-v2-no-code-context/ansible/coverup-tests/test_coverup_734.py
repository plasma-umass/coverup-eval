# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [325, 326], "branches": []}
# gained: {"lines": [325, 326], "branches": []}

import pytest
from ansible.playbook.play import Play

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestPlay(Play, MockBase, MockTaggable, MockCollectionSearch):
    def __init__(self):
        self.roles = ['role1', 'role2', 'role3']

def test_get_roles():
    play = TestPlay()
    roles = play.get_roles()
    assert roles == ['role1', 'role2', 'role3']
    assert roles is not play.roles  # Ensure a copy is returned
