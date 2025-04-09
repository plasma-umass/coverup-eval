# file: docstring_parser/numpydoc.py:201-204
# asked: {"lines": [201, 202, 204], "branches": []}
# gained: {"lines": [201, 202, 204], "branches": []}

import pytest
from docstring_parser.numpydoc import YieldsSection, ReturnsSection

def test_yields_section_inheritance():
    # Ensure YieldsSection inherits from ReturnsSection
    assert issubclass(YieldsSection, ReturnsSection)

def test_yields_section_is_generator():
    # Ensure is_generator is True in YieldsSection
    assert YieldsSection.is_generator is True

def test_returns_section_is_generator():
    # Ensure is_generator is False in ReturnsSection
    assert ReturnsSection.is_generator is False
