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

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up any state if necessary
    yield
    # Reset any changes made by the tests
    monkeypatch.undo()

# Mocking the group function to ensure it is called correctly
def test_maybe_group_call(mocker):
    from blib2to3.pgen2.tokenize import maybe
    mock_group = mocker.patch('blib2to3.pgen2.tokenize.group', return_value="mocked_group")
    result = maybe("a", "b")
    mock_group.assert_called_once_with("a", "b")
    assert result == "mocked_group?"
