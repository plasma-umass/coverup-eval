# file: docstring_parser/common.py:98-110
# asked: {"lines": [98, 99, 101, 108, 109, 110], "branches": []}
# gained: {"lines": [98, 99, 101, 108, 109, 110], "branches": []}

import pytest
from docstring_parser.common import DocstringDeprecated

def test_docstring_deprecated_init():
    args = ["arg1", "arg2"]
    description = "This is a deprecated function."
    version = "1.0.0"
    
    deprecated = DocstringDeprecated(args, description, version)
    
    assert deprecated.args == args
    assert deprecated.description == description
    assert deprecated.version == version

def test_docstring_deprecated_no_version():
    args = ["arg1", "arg2"]
    description = "This is a deprecated function."
    version = None
    
    deprecated = DocstringDeprecated(args, description, version)
    
    assert deprecated.args == args
    assert deprecated.description == description
    assert deprecated.version is None

def test_docstring_deprecated_no_description():
    args = ["arg1", "arg2"]
    description = None
    version = "1.0.0"
    
    deprecated = DocstringDeprecated(args, description, version)
    
    assert deprecated.args == args
    assert deprecated.description is None
    assert deprecated.version == version

def test_docstring_deprecated_no_args():
    args = []
    description = "This is a deprecated function."
    version = "1.0.0"
    
    deprecated = DocstringDeprecated(args, description, version)
    
    assert deprecated.args == args
    assert deprecated.description == description
    assert deprecated.version == version
