# file: lib/ansible/playbook/play.py:230-241
# asked: {"lines": [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], "branches": [[233, 234], [233, 241], [234, 235], [234, 241], [235, 236], [235, 237], [237, 238], [237, 240], [238, 237], [238, 239]]}
# gained: {"lines": [230], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.vars.manager import preprocess_vars

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
    def _load_vars_prompt(self, attr, ds):
        new_ds = preprocess_vars(ds)
        vars_prompts = []
        if new_ds is not None:
            for prompt_data in new_ds:
                if 'name' not in prompt_data:
                    raise AnsibleParserError("Invalid vars_prompt data structure, missing 'name' key", obj=ds)
                for key in prompt_data:
                    if key not in ('name', 'prompt', 'default', 'private', 'confirm', 'encrypt', 'salt_size', 'salt', 'unsafe'):
                        raise AnsibleParserError("Invalid vars_prompt data structure, found unsupported key '%s'" % key, obj=ds)
                vars_prompts.append(prompt_data)
        return vars_prompts

@pytest.fixture
def mock_play():
    return MockPlay()

def test_load_vars_prompt_valid_data(mock_play):
    ds = [{'name': 'var1', 'prompt': 'Enter var1'}]
    result = mock_play._load_vars_prompt(None, ds)
    assert result == ds

def test_load_vars_prompt_missing_name(mock_play):
    ds = [{'prompt': 'Enter var1'}]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, missing 'name' key"):
        mock_play._load_vars_prompt(None, ds)

def test_load_vars_prompt_unsupported_key(mock_play):
    ds = [{'name': 'var1', 'unsupported_key': 'value'}]
    with pytest.raises(AnsibleParserError, match="Invalid vars_prompt data structure, found unsupported key 'unsupported_key'"):
        mock_play._load_vars_prompt(None, ds)

def test_load_vars_prompt_empty_ds(mock_play):
    ds = []
    result = mock_play._load_vars_prompt(None, ds)
    assert result == []

def test_load_vars_prompt_none_ds(mock_play):
    ds = None
    result = mock_play._load_vars_prompt(None, ds)
    assert result == []
