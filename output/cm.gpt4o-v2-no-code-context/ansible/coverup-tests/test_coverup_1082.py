# file: lib/ansible/playbook/play.py:230-241
# asked: {"lines": [], "branches": [[233, 241]]}
# gained: {"lines": [], "branches": [[233, 241]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

class TestPlay:
    def test_load_vars_prompt_with_valid_data(self):
        play = Play()
        ds = [{'name': 'var1', 'prompt': 'Enter var1', 'default': 'default1'}]
        result = play._load_vars_prompt('attr', ds)
        assert result == ds

    def test_load_vars_prompt_with_invalid_data_missing_name(self):
        play = Play()
        ds = [{'prompt': 'Enter var1', 'default': 'default1'}]
        with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, missing 'name' key"):
            play._load_vars_prompt('attr', ds)

    def test_load_vars_prompt_with_invalid_data_unsupported_key(self):
        play = Play()
        ds = [{'name': 'var1', 'prompt': 'Enter var1', 'default': 'default1', 'unsupported_key': 'value'}]
        with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, found unsupported key 'unsupported_key'"):
            play._load_vars_prompt('attr', ds)

    def test_load_vars_prompt_with_none_data(self):
        play = Play()
        ds = None
        result = play._load_vars_prompt('attr', ds)
        assert result == []

    def test_load_vars_prompt_with_empty_list(self):
        play = Play()
        ds = []
        result = play._load_vars_prompt('attr', ds)
        assert result == []
