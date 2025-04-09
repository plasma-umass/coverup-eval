# file src/blib2to3/pgen2/pgen.py:136-141
# lines [136, 137, 138, 139, 140, 141]
# branches ['139->exit', '139->140', '140->139', '140->141']

import pytest
from blib2to3.pgen2 import pgen

# Assuming the ParserGenerator class is part of a larger module, we'll need to mock out
# dependencies and ensure the test is isolated.

class TestParserGenerator:
    @pytest.fixture
    def parser_gen(self, mocker):
        # Mocking the dependencies of ParserGenerator
        mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.calcfirst')
        # Mocking the __init__ method to not require the 'filename' argument
        mocker.patch.object(pgen.ParserGenerator, '__init__', return_value=None)
        return pgen.ParserGenerator()

    def test_addfirstsets(self, parser_gen, mocker):
        # Setup: Ensure that 'first' does not contain the key we will add
        test_key = 'test_key'
        parser_gen.dfas = {test_key: None}
        parser_gen.first = {}

        # Mock the 'calcfirst' method to check if it's called with the correct argument
        mock_calcfirst = mocker.patch.object(parser_gen, 'calcfirst')

        # Exercise: Call the method under test
        parser_gen.addfirstsets()

        # Verify: Check that 'calcfirst' was called with the correct key
        mock_calcfirst.assert_called_once_with(test_key)

        # Cleanup: No cleanup required as we are using mocks and not modifying any global state
