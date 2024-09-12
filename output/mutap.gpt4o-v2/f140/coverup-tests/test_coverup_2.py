# file: f140/__init__.py:1-22
# asked: {"lines": [21], "branches": [[20, 21]]}
# gained: {"lines": [21], "branches": [[20, 21]]}

import pytest
from f140 import fix_spaces

def test_fix_spaces_no_spaces():
    assert fix_spaces("hello") == "hello"

def test_fix_spaces_single_space():
    assert fix_spaces("hello world") == "hello_world"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("hello   world") == "hello-world"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("hello ") == "hello_"
    assert fix_spaces("hello  ") == "hello_"
    assert fix_spaces("hello   ") == "hello-"

def test_fix_spaces_leading_spaces():
    assert fix_spaces(" hello") == "_hello"
    assert fix_spaces("  hello") == "__hello"
    assert fix_spaces("   hello") == "-hello"

def test_fix_spaces_internal_and_trailing_spaces():
    assert fix_spaces("hello  world ") == "hello__world_"
    assert fix_spaces("hello   world  ") == "hello-world_"
    assert fix_spaces("hello    world   ") == "hello-world-"
