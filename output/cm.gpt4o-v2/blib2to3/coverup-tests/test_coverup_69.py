# file: src/blib2to3/pgen2/pgen.py:366-372
# asked: {"lines": [366, 367, 368, 369, 370, 371, 372], "branches": [[367, 368], [367, 372]]}
# gained: {"lines": [366, 367, 368, 369, 372], "branches": [[367, 368], [367, 372]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def parser_generator(tmp_path, mocker):
    file = tmp_path / "test_file.py"
    file.write_text("print('Hello, world!')\n")
    mocker.patch.object(ParserGenerator, 'parse', return_value=({}, 'file_input'))
    return ParserGenerator(filename=str(file))

def test_raise_error_with_args(parser_generator, mocker):
    mocker.patch.object(parser_generator, 'filename', 'test_file.py')
    mocker.patch.object(parser_generator, 'end', (1, 2))
    mocker.patch.object(parser_generator, 'line', 'print("Hello, world!")')

    with pytest.raises(SyntaxError) as excinfo:
        parser_generator.raise_error("Error: %s", "unexpected indent")
    
    assert excinfo.value.args[0] == "Error: unexpected indent"
    assert excinfo.value.args[1] == ('test_file.py', 1, 2, 'print("Hello, world!")')

def test_raise_error_without_args(parser_generator, mocker):
    mocker.patch.object(parser_generator, 'filename', 'test_file.py')
    mocker.patch.object(parser_generator, 'end', (1, 2))
    mocker.patch.object(parser_generator, 'line', 'print("Hello, world!")')

    with pytest.raises(SyntaxError) as excinfo:
        parser_generator.raise_error("Error: unexpected indent")
    
    assert excinfo.value.args[0] == "Error: unexpected indent"
    assert excinfo.value.args[1] == ('test_file.py', 1, 2, 'print("Hello, world!")')

def test_raise_error_with_formatting_issue(parser_generator, mocker):
    mocker.patch.object(parser_generator, 'filename', 'test_file.py')
    mocker.patch.object(parser_generator, 'end', (1, 2))
    mocker.patch.object(parser_generator, 'line', 'print("Hello, world!")')

    with pytest.raises(SyntaxError) as excinfo:
        parser_generator.raise_error("Error: %s %s", "unexpected", "indent")
    
    assert excinfo.value.args[0] == "Error: unexpected indent"
    assert excinfo.value.args[1] == ('test_file.py', 1, 2, 'print("Hello, world!")')
