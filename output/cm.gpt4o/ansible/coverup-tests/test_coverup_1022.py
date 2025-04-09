# file lib/ansible/parsing/mod_args.py:60-106
# lines [60, 62]
# branches []

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError

@pytest.fixture
def module_args_parser():
    return ModuleArgsParser()

def test_legacy_form(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'action': 'shell echo hi'})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}

def test_local_action(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'local_action': 'shell echo hi'})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}
    assert delegate_to == 'localhost'

def test_common_shorthand(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'copy': 'src=a dest=b'})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_legacy_form_with_args(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'action': 'copy src=a dest=b'})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_complex_args_form(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'copy': {'src': 'a', 'dest': 'b'}})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_gross_but_legal(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'action': {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_standard_yaml_form(module_args_parser, mocker):
    mocker.patch.object(module_args_parser, '_task_ds', {'command': 'pwd', 'args': {'chdir': '/tmp'}})
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'command'
    assert args == {'_raw_params': 'pwd', 'chdir': '/tmp'}
