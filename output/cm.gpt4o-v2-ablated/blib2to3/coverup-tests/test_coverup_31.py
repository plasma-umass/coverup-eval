# file: src/blib2to3/pgen2/tokenize.py:184-189
# asked: {"lines": [185, 186, 187, 188], "branches": []}
# gained: {"lines": [185, 186, 187, 188], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import tok_name

def test_printtoken(monkeypatch):
    from blib2to3.pgen2.tokenize import printtoken

    def mock_print(*args, **kwargs):
        mock_print.output = args[0]

    monkeypatch.setattr("builtins.print", mock_print)

    # Test data
    type = 1
    token = "test_token"
    xxx_todo_changeme = (1, 0)
    xxx_todo_changeme1 = (1, 10)
    line = "test line"

    # Call the function
    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)

    # Verify the output
    expected_output = "1,0-1,10:\t%s\t%s" % (tok_name[type], repr(token))
    assert mock_print.output == expected_output
