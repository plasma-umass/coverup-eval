# file: src/blib2to3/pgen2/pgen.py:366-372
# asked: {"lines": [366, 367, 368, 369, 370, 371, 372], "branches": [[367, 368], [367, 372]]}
# gained: {"lines": [366, 367, 368, 369, 370, 371, 372], "branches": [[367, 368], [367, 372]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

class MockParserGenerator(ParserGenerator):
    def __init__(self):
        self.filename = "testfile"
        self.end = (1, 1)
        self.line = "test line"

def test_raise_error_no_args():
    parser = MockParserGenerator()
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error("error message")
    assert str(excinfo.value) == "error message (testfile, line 1)"

def test_raise_error_with_args():
    parser = MockParserGenerator()
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error("error %s", "message")
    assert str(excinfo.value) == "error message (testfile, line 1)"

def test_raise_error_with_args_formatting_error():
    parser = MockParserGenerator()
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error("error %d", "message")
    assert str(excinfo.value) == "error %d message (testfile, line 1)"
