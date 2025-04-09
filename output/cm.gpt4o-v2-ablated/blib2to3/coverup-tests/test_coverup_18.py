# file: src/blib2to3/pgen2/tokenize.py:184-189
# asked: {"lines": [184, 185, 186, 187, 188], "branches": []}
# gained: {"lines": [184], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import tok_name

def printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line):  # for testing
    (srow, scol) = xxx_todo_changeme
    (erow, ecol) = xxx_todo_changeme1
    print(
        "%d,%d-%d,%d:\t%s\t%s" % (srow, scol, erow, ecol, tok_name[type], repr(token))
    )

def test_printtoken(monkeypatch):
    # Mocking print to capture the output for assertion
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))

    # Test data
    type = 1
    token = "test_token"
    xxx_todo_changeme = (1, 2)
    xxx_todo_changeme1 = (3, 4)
    line = "test_line"

    # Call the function
    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)

    # Assertions
    assert len(printed) == 1
    assert printed[0] == "1,2-3,4:\t%s\t%s" % (tok_name[type], repr(token))
