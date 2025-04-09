# file: lib/ansible/playbook/play.py:230-241
# asked: {"lines": [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], "branches": [[233, 234], [233, 241], [234, 235], [234, 241], [235, 236], [235, 237], [237, 238], [237, 240], [238, 237], [238, 239]]}
# gained: {"lines": [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], "branches": [[233, 234], [234, 235], [234, 241], [235, 236], [235, 237], [237, 238], [237, 240], [238, 237], [238, 239]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

class TestPlay:
    def test_load_vars_prompt_valid_data(self):
        play = Play()
        ds = [
            {'name': 'var1', 'prompt': 'Enter var1', 'default': 'value1'},
            {'name': 'var2', 'prompt': 'Enter var2', 'default': 'value2'}
        ]
        result = play._load_vars_prompt('attr', ds)
        assert result == ds

    def test_load_vars_prompt_missing_name(self):
        play = Play()
        ds = [
            {'prompt': 'Enter var1', 'default': 'value1'}
        ]
        with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, missing 'name' key"):
            play._load_vars_prompt('attr', ds)

    def test_load_vars_prompt_unsupported_key(self):
        play = Play()
        ds = [
            {'name': 'var1', 'prompt': 'Enter var1', 'default': 'value1', 'unsupported_key': 'value'}
        ]
        with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, found unsupported key 'unsupported_key'"):
            play._load_vars_prompt('attr', ds)
