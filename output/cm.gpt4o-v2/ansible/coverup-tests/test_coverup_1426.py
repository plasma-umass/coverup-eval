# file: lib/ansible/parsing/mod_args.py:140-193
# asked: {"lines": [160], "branches": [[159, 160]]}
# gained: {"lines": [160], "branches": [[159, 160]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError

def test_normalize_parameters_with_dict_additional_args():
    parser = ModuleArgsParser()
    thing = {}
    action = None
    additional_args = {'key': 'value'}

    result_action, result_args = parser._normalize_parameters(thing, action, additional_args)

    assert result_args == {'key': 'value'}

def test_normalize_parameters_with_invalid_additional_args():
    parser = ModuleArgsParser()
    thing = {}
    action = None
    additional_args = 123  # Invalid type

    with pytest.raises(AnsibleParserError, match='Complex args must be a dictionary or variable string'):
        parser._normalize_parameters(thing, action, additional_args)
