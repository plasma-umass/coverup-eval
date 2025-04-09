# file: lib/ansible/parsing/mod_args.py:222-258
# asked: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [241, 258], [248, 250], [248, 256]]}
# gained: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [248, 250], [248, 256]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.module_utils.common.text.converters import to_text

def test_normalize_old_style_args_dict_with_module(monkeypatch):
    parser = ModuleArgsParser()
    
    def mock_split_module_string(module_string):
        return 'copy', 'src=a dest=b'
    
    def mock_parse_kv(args, check_raw=False):
        return {'src': 'a', 'dest': 'b'}
    
    monkeypatch.setattr(parser, '_split_module_string', mock_split_module_string)
    monkeypatch.setattr('ansible.parsing.mod_args.parse_kv', mock_parse_kv)
    
    thing = {'module': 'copy', 'src': 'a', 'dest': 'b'}
    action, args = parser._normalize_old_style_args(thing)
    
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_string(monkeypatch):
    parser = ModuleArgsParser()
    
    def mock_split_module_string(module_string):
        return 'copy', 'src=a dest=b'
    
    def mock_parse_kv(args, check_raw=False):
        return {'src': 'a', 'dest': 'b'}
    
    monkeypatch.setattr(parser, '_split_module_string', mock_split_module_string)
    monkeypatch.setattr('ansible.parsing.mod_args.parse_kv', mock_parse_kv)
    
    thing = 'copy src=a dest=b'
    action, args = parser._normalize_old_style_args(thing)
    
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_unexpected_type():
    parser = ModuleArgsParser()
    
    thing = 12345  # An unexpected type (neither dict nor string)
    
    with pytest.raises(AnsibleParserError) as excinfo:
        parser._normalize_old_style_args(thing)
    
    assert "unexpected parameter type in action" in to_text(excinfo.value)

