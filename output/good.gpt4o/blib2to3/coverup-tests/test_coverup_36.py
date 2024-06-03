# file src/blib2to3/pgen2/tokenize.py:184-189
# lines [184, 185, 186, 187, 188]
# branches []

import pytest
from blib2to3.pgen2.tokenize import tok_name

def test_printtoken(capsys):
    def printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line):  # for testing
        (srow, scol) = xxx_todo_changeme
        (erow, ecol) = xxx_todo_changeme1
        print(
            "%d,%d-%d,%d:\t%s\t%s" % (srow, scol, erow, ecol, tok_name[type], repr(token))
        )

    # Define test parameters
    type = 1  # Example token type
    token = "example_token"
    xxx_todo_changeme = (1, 0)
    xxx_todo_changeme1 = (1, 13)
    line = "example line"

    # Call the function
    printtoken(type, token, xxx_todo_changeme, xxx_todo_changeme1, line)

    # Capture the output
    captured = capsys.readouterr()

    # Assert the expected output
    expected_output = "1,0-1,13:\t%s\t%s\n" % (tok_name[type], repr(token))
    assert captured.out == expected_output
