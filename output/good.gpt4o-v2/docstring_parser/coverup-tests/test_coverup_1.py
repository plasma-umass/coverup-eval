# file: docstring_parser/common.py:98-110
# asked: {"lines": [98, 99, 101, 108, 109, 110], "branches": []}
# gained: {"lines": [98, 99, 101, 108, 109, 110], "branches": []}

import pytest
from docstring_parser.common import DocstringDeprecated

def test_docstring_deprecated_initialization():
    args = ["arg1", "arg2"]
    description = "This is a deprecated function."
    version = "1.0.0"
    
    deprecated_meta = DocstringDeprecated(args, description, version)
    
    assert deprecated_meta.args == args
    assert deprecated_meta.description == description
    assert deprecated_meta.version == version
