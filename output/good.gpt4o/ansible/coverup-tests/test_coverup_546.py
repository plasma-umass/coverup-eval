# file lib/ansible/parsing/mod_args.py:126-138
# lines [126, 134, 135, 136, 138]
# branches ['135->136', '135->138']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser

def test_split_module_string(mocker):
    parser = ModuleArgsParser()

    # Test case where module_string has multiple tokens
    module_string = "copy src=a dest=b"
    result = parser._split_module_string(module_string)
    assert result == ("copy", "src=a dest=b")

    # Test case where module_string has a single token
    module_string = "copy"
    result = parser._split_module_string(module_string)
    assert result == ("copy", "")

    # Clean up any mock if used
    mocker.stopall()
