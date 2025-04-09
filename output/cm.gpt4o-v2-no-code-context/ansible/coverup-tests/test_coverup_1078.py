# file: lib/ansible/playbook/play.py:312-313
# asked: {"lines": [313], "branches": []}
# gained: {"lines": [313], "branches": []}

import pytest
from ansible.playbook.play import Play

class TestPlay:
    @pytest.fixture
    def play_instance(self):
        class MockPlay(Play):
            def __init__(self):
                self.vars = {'key1': 'value1', 'key2': 'value2'}
        
        return MockPlay()

    def test_get_vars(self, play_instance):
        vars_copy = play_instance.get_vars()
        assert vars_copy == {'key1': 'value1', 'key2': 'value2'}
        assert vars_copy is not play_instance.vars  # Ensure it's a copy, not the same object
