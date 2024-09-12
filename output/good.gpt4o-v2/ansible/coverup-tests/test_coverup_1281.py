# file: lib/ansible/playbook/play.py:230-241
# asked: {"lines": [], "branches": [[233, 241]]}
# gained: {"lines": [], "branches": [[233, 241]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

def test_load_vars_prompt_with_valid_data():
    play = Play()
    ds = [{'name': 'var1', 'prompt': 'Enter var1'}]
    result = play._load_vars_prompt(None, ds)
    assert result == ds

def test_load_vars_prompt_with_none():
    play = Play()
    result = play._load_vars_prompt(None, None)
    assert result == []

def test_load_vars_prompt_missing_name_key():
    play = Play()
    ds = [{'prompt': 'Enter var1'}]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, missing 'name' key"):
        play._load_vars_prompt(None, ds)

def test_load_vars_prompt_with_unsupported_key():
    play = Play()
    ds = [{'name': 'var1', 'unsupported_key': 'value'}]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, found unsupported key 'unsupported_key'"):
        play._load_vars_prompt(None, ds)
