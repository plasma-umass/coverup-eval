# file: lib/ansible/parsing/mod_args.py:195-220
# asked: {"lines": [195, 208, 210, 211, 213, 214, 215, 217, 219, 220], "branches": [[208, 210], [208, 211], [211, 213], [211, 215], [215, 217], [215, 219]]}
# gained: {"lines": [195, 208, 210, 211, 213, 214, 215, 217, 219, 220], "branches": [[208, 210], [208, 211], [211, 213], [211, 215], [215, 217], [215, 219]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types

# Mocking dependencies
FREEFORM_ACTIONS = ['shell', 'command']
def parse_kv(thing, check_raw=False):
    if check_raw:
        return {'_raw_params': thing, '_uses_shell': True}
    return dict(pair.split('=') for pair in thing.split())

class TestModuleArgsParser:
    @pytest.fixture
    def parser(self):
        return ModuleArgsParser()

    def test_normalize_new_style_args_dict(self, parser):
        thing = {'region': 'xyz'}
        action = 'ec2'
        result = parser._normalize_new_style_args(thing, action)
        assert result == {'region': 'xyz'}

    def test_normalize_new_style_args_string_freeform(self, parser, monkeypatch):
        thing = 'echo hi'
        action = 'shell'
        monkeypatch.setattr('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
        monkeypatch.setattr('ansible.parsing.mod_args.parse_kv', parse_kv)
        result = parser._normalize_new_style_args(thing, action)
        assert result == {'_raw_params': 'echo hi', '_uses_shell': True}

    def test_normalize_new_style_args_string_non_freeform(self, parser, monkeypatch):
        thing = 'src=a dest=b'
        action = 'copy'
        monkeypatch.setattr('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
        monkeypatch.setattr('ansible.parsing.mod_args.parse_kv', parse_kv)
        result = parser._normalize_new_style_args(thing, action)
        assert result == {'src': 'a', 'dest': 'b'}

    def test_normalize_new_style_args_none(self, parser):
        thing = None
        action = 'ping'
        result = parser._normalize_new_style_args(thing, action)
        assert result is None

    def test_normalize_new_style_args_unexpected_type(self, parser):
        thing = 12345
        action = 'copy'
        with pytest.raises(AnsibleParserError, match="unexpected parameter type in action: <class 'int'>"):
            parser._normalize_new_style_args(thing, action)
