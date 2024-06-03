# file src/blib2to3/pgen2/pgen.py:366-372
# lines [367, 368, 369, 370, 371, 372]
# branches ['367->368', '367->372']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

def test_raise_error_with_args(mocker):
    # Mocking the attributes used in the raise_error method
    parser_generator = mocker.Mock(spec=ParserGenerator)
    parser_generator.filename = "test_file.py"
    parser_generator.end = (10, 20)
    parser_generator.line = "some line of code"

    # Test case where args are provided and msg formatting succeeds
    with pytest.raises(SyntaxError) as excinfo:
        ParserGenerator.raise_error(parser_generator, "Error at %s", "location")
    assert excinfo.value.args[0] == "Error at location"
    assert excinfo.value.args[1] == ("test_file.py", 10, 20, "some line of code")

    # Test case where args are provided and msg formatting fails
    with pytest.raises(SyntaxError) as excinfo:
        ParserGenerator.raise_error(parser_generator, "Error at %s %s", "location")
    assert excinfo.value.args[0] == "Error at %s %s location"
    assert excinfo.value.args[1] == ("test_file.py", 10, 20, "some line of code")
