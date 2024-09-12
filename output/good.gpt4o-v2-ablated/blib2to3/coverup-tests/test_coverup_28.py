# file: src/blib2to3/pgen2/tokenize.py:70-71
# asked: {"lines": [70, 71], "branches": []}
# gained: {"lines": [70, 71], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_maybe_single_choice():
    from blib2to3.pgen2.tokenize import maybe
    result = maybe("a")
    assert result == "(a)?"

def test_maybe_multiple_choices():
    from blib2to3.pgen2.tokenize import maybe
    result = maybe("a", "b", "c")
    assert result == "(a|b|c)?"

def test_maybe_no_choices():
    from blib2to3.pgen2.tokenize import maybe
    result = maybe()
    assert result == "()?"

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Perform any necessary cleanup after tests
