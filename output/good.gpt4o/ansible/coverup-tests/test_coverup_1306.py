# file lib/ansible/playbook/play.py:230-241
# lines []
# branches ['233->241']

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def play_instance():
    return Play()

def test_load_vars_prompt_with_valid_data(play_instance):
    ds = [
        {'name': 'var1', 'prompt': 'Enter var1', 'default': 'default1'},
        {'name': 'var2', 'prompt': 'Enter var2', 'default': 'default2'}
    ]
    result = play_instance._load_vars_prompt('attr', ds)
    assert result == ds

def test_load_vars_prompt_with_missing_name_key(play_instance):
    ds = [
        {'prompt': 'Enter var1', 'default': 'default1'}
    ]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, missing 'name' key"):
        play_instance._load_vars_prompt('attr', ds)

def test_load_vars_prompt_with_unsupported_key(play_instance):
    ds = [
        {'name': 'var1', 'prompt': 'Enter var1', 'default': 'default1', 'unsupported_key': 'value'}
    ]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, found unsupported key 'unsupported_key'"):
        play_instance._load_vars_prompt('attr', ds)

def test_load_vars_prompt_with_none_data(play_instance):
    ds = None
    result = play_instance._load_vars_prompt('attr', ds)
    assert result == []
