# file: src/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [51], "branches": [[50, 51]]}
# gained: {"lines": [51], "branches": [[50, 51]]}

import pytest
from blib2to3.pgen2.literals import evalString

def test_evalString_single_quote():
    result = evalString("'hello'")
    assert result == "hello"

def test_evalString_double_quote():
    result = evalString('"hello"')
    assert result == "hello"

def test_evalString_triple_single_quote():
    result = evalString("'''hello'''")
    assert result == "hello"

def test_evalString_triple_double_quote():
    result = evalString('"""hello"""')
    assert result == "hello"

def test_evalString_escaped_characters():
    result = evalString(r"'hello\nworld'")
    assert result == "hello\nworld"

def test_evalString_triple_single_quote_with_escape():
    result = evalString(r"'''hello\nworld'''")
    assert result == "hello\nworld"

def test_evalString_triple_double_quote_with_escape():
    result = evalString(r'"""hello\nworld"""')
    assert result == "hello\nworld"
