# file src/blib2to3/pgen2/pgen.py:366-372
# lines [366, 367, 368, 369, 370, 371, 372]
# branches ['367->368', '367->372']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

def test_raise_error_with_args(mocker):
    mocker.patch.object(ParserGenerator, '__init__', lambda x: None)
    pg = ParserGenerator()
    pg.filename = "testfile"
    pg.end = (1, 2)
    pg.line = "error line"

    with pytest.raises(SyntaxError) as exc_info:
        pg.raise_error("Error: %s", "test")

    assert exc_info.value.args[0] == "Error: test"
    assert exc_info.value.args[1] == ("testfile", 1, 2, "error line")

def test_raise_error_with_invalid_format_args(mocker):
    mocker.patch.object(ParserGenerator, '__init__', lambda x: None)
    pg = ParserGenerator()
    pg.filename = "testfile"
    pg.end = (1, 2)
    pg.line = "error line"

    with pytest.raises(SyntaxError) as exc_info:
        pg.raise_error("Error: %s %s", "test")

    assert "Error: %s %s test" in str(exc_info.value)
    assert exc_info.value.args[1] == ("testfile", 1, 2, "error line")
