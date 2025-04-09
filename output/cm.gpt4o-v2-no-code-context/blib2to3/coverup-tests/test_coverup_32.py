# file: src/blib2to3/pgen2/tokenize.py:184-189
# asked: {"lines": [184, 185, 186, 187, 188], "branches": []}
# gained: {"lines": [184, 185, 186, 187, 188], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import printtoken, tok_name

def test_printtoken(monkeypatch):
    # Mock the print function to capture its output
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))

    # Define the inputs
    type = 1  # Assuming 1 is a valid token type
    token = "test_token"
    xxx_todo_changeme = (1, 2)
    xxx_todo_changeme1 = (3, 4)
    line = "test_line"

    # Call the function
    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)

    # Verify the output
    assert printed == ["1,2-3,4:\t%s\t%s" % (tok_name[type], repr(token))]
