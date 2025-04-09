# file apimd/parser.py:518-526
# lines [522]
# branches ['521->522', '525->520']

import pytest
from apimd.parser import Parser
from types import ModuleType
from unittest.mock import MagicMock

def test_load_docstring_full_coverage(mocker):
    # Mock the getdoc function to control its return value
    mocker.patch('apimd.parser.getdoc', return_value='mocked_docstring')
    # Mock the _attr function to control its return value
    mocker.patch('apimd.parser._attr', return_value=MagicMock())
    # Mock the doctest function to control its return value
    mocker.patch('apimd.parser.doctest', return_value='mocked_doctest')

    # Create a Parser instance with a doc dictionary that will trigger the missing lines
    parser = Parser()
    parser.doc = {'root.module': 'docstring', 'other.module': 'docstring'}
    parser.docstring = {}

    # Create a mock module
    mock_module = ModuleType('mock_module')

    # Call the load_docstring method with the mock module
    parser.load_docstring('root', mock_module)

    # Assert that the docstring for 'root.module' is set correctly
    assert parser.docstring == {'root.module': 'mocked_doctest'}
    # Assert that the 'other.module' was skipped due to the continue statement
    assert 'other.module' not in parser.docstring

    # Cleanup is handled by pytest-mock through its patching mechanism
