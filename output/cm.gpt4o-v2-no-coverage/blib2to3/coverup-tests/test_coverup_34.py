# file: src/blib2to3/pgen2/tokenize.py:184-189
# asked: {"lines": [184, 185, 186, 187, 188], "branches": []}
# gained: {"lines": [184, 185, 186, 187, 188], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import printtoken
from blib2to3.pgen2.token import tok_name, NAME

def test_printtoken(capsys):
    type = NAME
    token = "example"
    xxx_todo_changeme = (1, 0)
    xxx_todo_changeme1 = (1, 7)
    line = "example line"

    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)
    
    captured = capsys.readouterr()
    assert captured.out == "1,0-1,7:\tNAME\t'example'\n"
