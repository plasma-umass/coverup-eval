# file: docstring_parser/numpydoc.py:272-279
# asked: {"lines": [272, 278, 279], "branches": []}
# gained: {"lines": [272, 278, 279], "branches": []}

import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

@pytest.fixture
def parser():
    return NumpydocParser()

def test_add_section(parser, mocker):
    # Create a mock section object
    section = mocker.Mock(spec=Section)
    section.title = "Test Section"
    
    # Mock the _setup method to ensure it is called
    mock_setup = mocker.patch.object(parser, '_setup')
    
    parser.add_section(section)
    
    # Verify the section was added
    assert parser.sections["Test Section"] == section
    
    # Verify the _setup method was called
    mock_setup.assert_called_once()
