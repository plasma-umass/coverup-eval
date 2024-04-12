# file docstring_parser/numpydoc.py:201-204
# lines [201, 202, 204]
# branches []

import pytest
from docstring_parser.numpydoc import YieldsSection

def test_yields_section_is_generator():
    yields_section = YieldsSection('Yields', 'yields')
    assert yields_section.is_generator == True
