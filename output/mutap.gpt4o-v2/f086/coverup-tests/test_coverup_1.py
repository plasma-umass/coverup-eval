# file: f086/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f086.__init__ import anti_shuffle

def test_anti_shuffle():
    # Test with a simple string
    result = anti_shuffle("cba fed")
    assert result == "abc def"

    # Test with an empty string
    result = anti_shuffle("")
    assert result == ""

    # Test with a single word
    result = anti_shuffle("zyx")
    assert result == "xyz"

    # Test with multiple spaces
    result = anti_shuffle("a  b")
    assert result == "a  b"

    # Test with special characters
    result = anti_shuffle("!@# $%^")
    assert result == "!#@ $%^"
