# file src/blib2to3/pgen2/literals.py:47-55
# lines [47, 48, 49, 50, 51, 52, 53, 54, 55]
# branches ['50->51', '50->52']

import pytest
import re
from blib2to3.pgen2.literals import evalString

def escape(match):
    # This is a placeholder for the actual escape function used in evalString
    return match.group(0).encode().decode('unicode_escape')

def test_evalString_single_quotes():
    result = evalString("'hello\\nworld'")
    assert result == "hello\nworld"

def test_evalString_double_quotes():
    result = evalString('"hello\\nworld"')
    assert result == "hello\nworld"

def test_evalString_triple_single_quotes():
    result = evalString("'''hello\\nworld'''")
    assert result == "hello\nworld"

def test_evalString_triple_double_quotes():
    result = evalString('"""hello\\nworld"""')
    assert result == "hello\nworld"

def test_evalString_escaped_quotes():
    result = evalString("'hello\\'world'")
    assert result == "hello'world"

def test_evalString_escaped_backslash():
    result = evalString("'hello\\\\world'")
    assert result == "hello\\world"

def test_evalString_escaped_hex():
    result = evalString("'hello\\x41world'")
    assert result == "helloAworld"

def test_evalString_escaped_octal():
    result = evalString("'hello\\141world'")
    assert result == "helloaworld"

@pytest.fixture(autouse=True)
def mock_escape(mocker):
    mocker.patch('blib2to3.pgen2.literals.escape', side_effect=escape)
