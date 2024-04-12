# file docstring_parser/common.py:98-110
# lines [98, 99, 101, 108, 109, 110]
# branches []

import pytest
from docstring_parser.common import DocstringDeprecated

def test_docstring_deprecated_initialization():
    args = ["arg1", "arg2"]
    description = "This is a deprecated feature."
    version = "1.0.0"

    deprecated_meta = DocstringDeprecated(args, description, version)

    assert deprecated_meta.args == args
    assert deprecated_meta.description == description
    assert deprecated_meta.version == version

def test_docstring_deprecated_initialization_with_none():
    args = ["arg1", "arg2"]
    description = None
    version = None

    deprecated_meta = DocstringDeprecated(args, description, version)

    assert deprecated_meta.args == args
    assert deprecated_meta.description is None
    assert deprecated_meta.version is None
