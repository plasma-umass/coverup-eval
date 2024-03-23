# file src/blib2to3/pgen2/pgen.py:366-372
# lines []
# branches ['367->372']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

def test_raise_error_with_args(mocker):
    # Mocking the attributes required for the error message
    mocker.patch.object(ParserGenerator, '__init__', lambda self, filename: None)
    mocker.patch.object(ParserGenerator, 'filename', 'test_filename', create=True)
    mocker.patch.object(ParserGenerator, 'end', (1, 2), create=True)
    mocker.patch.object(ParserGenerator, 'line', 'test line', create=True)

    parser_gen = ParserGenerator('test_filename')

    # Test that the correct SyntaxError is raised with args that cause an exception in string formatting
    with pytest.raises(SyntaxError) as exc_info:
        parser_gen.raise_error("Error: %s %s", "arg1")

    assert exc_info.value.args[0] == "Error: %s %s arg1"
    assert exc_info.value.args[1] == ('test_filename', 1, 2, 'test line')

def test_raise_error_without_args(mocker):
    # Mocking the attributes required for the error message
    mocker.patch.object(ParserGenerator, '__init__', lambda self, filename: None)
    mocker.patch.object(ParserGenerator, 'filename', 'test_filename', create=True)
    mocker.patch.object(ParserGenerator, 'end', (1, 2), create=True)
    mocker.patch.object(ParserGenerator, 'line', 'test line', create=True)

    parser_gen = ParserGenerator('test_filename')

    # Test that the correct SyntaxError is raised without args
    with pytest.raises(SyntaxError) as exc_info:
        parser_gen.raise_error("Error without args")

    assert exc_info.value.args[0] == "Error without args"
    assert exc_info.value.args[1] == ('test_filename', 1, 2, 'test line')
