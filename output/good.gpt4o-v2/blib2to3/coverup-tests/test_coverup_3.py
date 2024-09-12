# file: src/blib2to3/pgen2/literals.py:58-64
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63], "branches": [[59, 0], [59, 60], [63, 59]]}

import pytest
from blib2to3.pgen2.literals import evalString

def test_evalString():
    # Test single quotes
    assert evalString("'a'") == 'a'
    assert evalString("'\\n'") == '\n'
    assert evalString("'\\x41'") == 'A'
    assert evalString("'\\141'") == 'a'
    
    # Test double quotes
    assert evalString('"a"') == 'a'
    assert evalString('"\\n"') == '\n'
    assert evalString('"\\x41"') == 'A'
    assert evalString('"\\141"') == 'a'
    
    # Test triple quotes
    assert evalString("'''a'''") == 'a'
    assert evalString('"""a"""') == 'a'
    assert evalString("'''\\n'''") == '\n'
    assert evalString('"""\\n"""') == '\n'
    assert evalString("'''\\x41'''") == 'A'
    assert evalString('"""\\x41"""') == 'A'
    assert evalString("'''\\141'''") == 'a'
    assert evalString('"""\\141"""') == 'a'

def test_test_function(monkeypatch):
    from blib2to3.pgen2.literals import test

    def mock_print(*args):
        pass

    monkeypatch.setattr("builtins.print", mock_print)
    test()
