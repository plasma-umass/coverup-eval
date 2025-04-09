# file: src/blib2to3/pgen2/pgen.py:366-372
# asked: {"lines": [366, 367, 368, 369, 370, 371, 372], "branches": [[367, 368], [367, 372]]}
# gained: {"lines": [366, 367, 368, 369, 370, 371, 372], "branches": [[367, 368], [367, 372]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

class MockParserGenerator(ParserGenerator):
    def __init__(self, filename, end, line):
        self.filename = filename
        self.end = end
        self.line = line

def test_raise_error_no_args():
    pg = MockParserGenerator("testfile.py", (1, 2), "some line of code")
    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Error message")
    assert excinfo.value.args[0] == "Error message"
    assert excinfo.value.args[1] == ("testfile.py", 1, 2, "some line of code")

def test_raise_error_with_args():
    pg = MockParserGenerator("testfile.py", (1, 2), "some line of code")
    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Error %s", "message")
    assert excinfo.value.args[0] == "Error message"
    assert excinfo.value.args[1] == ("testfile.py", 1, 2, "some line of code")

def test_raise_error_with_args_format_fail():
    pg = MockParserGenerator("testfile.py", (1, 2), "some line of code")
    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Error %s %s", "message")
    assert excinfo.value.args[0] == "Error %s %s message"
    assert excinfo.value.args[1] == ("testfile.py", 1, 2, "some line of code")
