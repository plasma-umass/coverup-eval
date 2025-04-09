# file lib/ansible/playbook/play.py:312-313
# lines [312, 313]
# branches []

import pytest
from ansible.playbook.play import Play

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestPlay(Play, MockBase, MockTaggable, MockCollectionSearch):
    def __init__(self, vars):
        self.vars = vars

def test_get_vars():
    vars_dict = {'key1': 'value1', 'key2': 'value2'}
    play_instance = TestPlay(vars_dict)
    
    result = play_instance.get_vars()
    
    assert result == vars_dict
    assert result is not vars_dict  # Ensure a copy is returned

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.stopall()
