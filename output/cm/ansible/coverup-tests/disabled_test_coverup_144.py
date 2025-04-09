# file lib/ansible/playbook/play.py:230-241
# lines [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241]
# branches ['233->234', '233->241', '234->235', '234->241', '235->236', '235->237', '237->238', '237->240', '238->237', '238->239']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from unittest.mock import MagicMock

# Mock the preprocess_vars function to control the input to _load_vars_prompt
def mock_preprocess_vars(ds):
    return ds

# Test function to cover missing branches in _load_vars_prompt
def test_load_vars_prompt_missing_name(mocker):
    mocker.patch('ansible.playbook.play.preprocess_vars', side_effect=mock_preprocess_vars)

    play = Play()

    # Test with missing 'name' key
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('vars_prompt', [{'prompt': 'Enter value'}])
    assert "Invalid vars_prompt data structure, missing 'name' key" in str(excinfo.value)

    # Test with unsupported key
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('vars_prompt', [{'name': 'test', 'unsupported_key': 'value'}])
    assert "Invalid vars_prompt data structure, found unsupported key 'unsupported_key'" in str(excinfo.value)

    # Test with valid data structure
    result = play._load_vars_prompt('vars_prompt', [{'name': 'test', 'prompt': 'Enter value'}])
    assert result == [{'name': 'test', 'prompt': 'Enter value'}]
