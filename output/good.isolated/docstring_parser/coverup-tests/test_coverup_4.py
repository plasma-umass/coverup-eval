# file docstring_parser/google.py:36-37
# lines [36, 37]
# branches []

import pytest
from docstring_parser.google import Section

def test_section_creation():
    # Create a Section instance to test its properties
    section = Section(title="Parameters", key="param", type="Arguments")

    # Assert that the properties are correctly assigned
    assert section.title == "Parameters"
    assert section.key == "param"
    assert section.type == "Arguments"

    # Create another Section with different values to test the namedtuple functionality
    another_section = Section(title="Returns", key="return", type="Return Values")

    # Assert that the new properties are correctly assigned
    assert another_section.title == "Returns"
    assert another_section.key == "return"
    assert another_section.type == "Return Values"

    # Assert that the two sections are different
    assert section != another_section
