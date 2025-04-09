# file: lib/ansible/parsing/mod_args.py:222-258
# asked: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [241, 258], [248, 250], [248, 256]]}
# gained: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [241, 258], [248, 250], [248, 256]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError

@pytest.fixture
def parser():
    return ModuleArgsParser()

def test_normalize_old_style_args_dict_with_module(parser, mocker):
    mocker.patch.object(parser, '_split_module_string', return_value=('ec2', 'x=1'))
    input_data = {'module': 'ec2', 'y': 2}
    action, args = parser._normalize_old_style_args(input_data)
    assert action == 'ec2'
    assert args == {'y': 2, 'x': '1'}

def test_normalize_old_style_args_dict_without_module(parser):
    input_data = {'shell': 'echo hi'}
    action, args = parser._normalize_old_style_args(input_data)
    assert action is None
    assert args is None

def test_normalize_old_style_args_string(parser, mocker):
    mocker.patch.object(parser, '_split_module_string', return_value=('copy', 'src=a dest=b'))
    input_data = 'copy src=a dest=b'
    action, args = parser._normalize_old_style_args(input_data)
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_invalid_type(parser):
    input_data = 12345
    with pytest.raises(AnsibleParserError, match="unexpected parameter type in action: <class 'int'>"):
        parser._normalize_old_style_args(input_data)
