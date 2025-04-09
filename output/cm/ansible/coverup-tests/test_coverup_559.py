# file lib/ansible/parsing/mod_args.py:126-138
# lines [126, 134, 135, 136, 138]
# branches ['135->136', '135->138']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.parsing.splitter import split_args

@pytest.fixture
def module_args_parser():
    return ModuleArgsParser()

def test_split_module_string_with_args(module_args_parser):
    module_string = "copy src=/src/path dest=/dest/path"
    module_name, module_args = module_args_parser._split_module_string(module_string)
    assert module_name == "copy"
    assert module_args == "src=/src/path dest=/dest/path"

def test_split_module_string_without_args(module_args_parser):
    module_string = "ping"
    module_name, module_args = module_args_parser._split_module_string(module_string)
    assert module_name == "ping"
    assert module_args == ""
