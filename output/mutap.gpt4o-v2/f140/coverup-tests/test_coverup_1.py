# file: f140/__init__.py:1-22
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 22]]}

import pytest
from f140 import fix_spaces

def test_fix_spaces_no_spaces():
    assert fix_spaces("hello") == "hello"

def test_fix_spaces_single_space():
    assert fix_spaces("hello world") == "hello_world"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("hello   world") == "hello-world"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("hello   ") == "hello-"

def test_fix_spaces_leading_spaces():
    assert fix_spaces("   hello") == "-hello"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("hello  world   !") == "hello__world-!"

def test_fix_spaces_no_text():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("     ") == "-"

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup
    yield
    # Teardown: nothing to teardown
