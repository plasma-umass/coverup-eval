# file: lib/ansible/parsing/mod_args.py:126-138
# asked: {"lines": [126, 134, 135, 136, 138], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [126, 134, 135, 136, 138], "branches": [[135, 136], [135, 138]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser

@pytest.fixture
def parser():
    return ModuleArgsParser()

def test_split_module_string_with_args(parser):
    module_string = "copy src=a dest=b"
    module_name, args = parser._split_module_string(module_string)
    assert module_name == "copy"
    assert args == "src=a dest=b"

def test_split_module_string_without_args(parser):
    module_string = "copy"
    module_name, args = parser._split_module_string(module_string)
    assert module_name == "copy"
    assert args == ""
