# file: src/blib2to3/pgen2/tokenize.py:184-189
# asked: {"lines": [184, 185, 186, 187, 188], "branches": []}
# gained: {"lines": [184, 185, 186, 187, 188], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import printtoken
from blib2to3.pgen2.token import tok_name

def test_printtoken(capsys):
    type = 1  # Example token type
    token = "example_token"
    xxx_todo_changeme = (1, 0)
    xxx_todo_changeme1 = (1, 12)
    line = "example_token"

    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)
    
    captured = capsys.readouterr()
    expected_output = "1,0-1,12:\t%s\t%s\n" % (tok_name[type], repr(token))
    assert captured.out == expected_output
