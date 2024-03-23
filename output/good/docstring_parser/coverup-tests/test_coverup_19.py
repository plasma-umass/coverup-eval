# file docstring_parser/numpydoc.py:272-279
# lines [272, 278, 279]
# branches []

import pytest
from unittest.mock import MagicMock
from docstring_parser.numpydoc import NumpydocParser

class MockSection:
    def __init__(self, title, content):
        self.title = title
        self.content = content

@pytest.fixture
def numpydoc_parser():
    return NumpydocParser()

def test_add_section(numpydoc_parser):
    # Create a mock _setup method
    numpydoc_parser._setup = MagicMock()

    # Create a mock section to add
    section = MockSection('Parameters', 'This is a test section')

    # Add the section to the parser
    numpydoc_parser.add_section(section)

    # Assert that the section was added
    assert numpydoc_parser.sections['Parameters'] == section

    # Assert that _setup was called once
    numpydoc_parser._setup.assert_called_once()
