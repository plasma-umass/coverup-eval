# file: src/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [51], "branches": [[50, 51]]}
# gained: {"lines": [51], "branches": [[50, 51]]}

import pytest
from blib2to3.pgen2.literals import evalString

def escape(match):
    return match.group(0)

def test_evalString_triple_quotes():
    # Test with triple single quotes
    input_str = "'''triple quoted string'''"
    expected_output = "triple quoted string"
    assert evalString(input_str) == expected_output

    # Test with triple double quotes
    input_str = '"""triple quoted string"""'
    expected_output = "triple quoted string"
    assert evalString(input_str) == expected_output

def test_evalString_single_quotes():
    # Test with single quotes
    input_str = "'single quoted string'"
    expected_output = "single quoted string"
    assert evalString(input_str) == expected_output

    # Test with double quotes
    input_str = '"double quoted string"'
    expected_output = "double quoted string"
    assert evalString(input_str) == expected_output

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: monkeypatch the escape function
    monkeypatch.setattr("blib2to3.pgen2.literals.escape", escape)
    yield
    # Teardown: nothing to clean up

