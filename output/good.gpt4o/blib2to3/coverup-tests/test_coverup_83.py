# file src/blib2to3/pgen2/tokenize.py:184-189
# lines [185, 186, 187, 188]
# branches []

import pytest
from blib2to3.pgen2.tokenize import printtoken, tok_name

def test_printtoken(mocker):
    mock_print = mocker.patch("builtins.print")
    
    type = 1
    token = "test_token"
    xxx_todo_changeme = (1, 2)
    xxx_todo_changeme1 = (3, 4)
    line = "test_line"
    
    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)
    
    mock_print.assert_called_once_with("1,2-3,4:\t%s\t%s" % (tok_name[type], repr(token)))
