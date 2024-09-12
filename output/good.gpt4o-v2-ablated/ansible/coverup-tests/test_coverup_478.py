# file: lib/ansible/parsing/mod_args.py:126-138
# asked: {"lines": [136], "branches": [[135, 136]]}
# gained: {"lines": [136], "branches": [[135, 136]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser

def split_args(module_string):
    # Mock implementation of split_args for testing purposes
    return module_string.split()

@pytest.fixture
def parser(monkeypatch):
    monkeypatch.setattr('ansible.parsing.mod_args.split_args', split_args)
    return ModuleArgsParser()

def test_split_module_string_with_arguments(parser):
    module_string = "action: copy src=a dest=b"
    module_name, args = parser._split_module_string(module_string)
    assert module_name == "action:"
    assert args == "copy src=a dest=b"

def test_split_module_string_without_arguments(parser):
    module_string = "action:"
    module_name, args = parser._split_module_string(module_string)
    assert module_name == "action:"
    assert args == ""

def test_split_module_string_single_word(parser):
    module_string = "action"
    module_name, args = parser._split_module_string(module_string)
    assert module_name == "action"
    assert args == ""
