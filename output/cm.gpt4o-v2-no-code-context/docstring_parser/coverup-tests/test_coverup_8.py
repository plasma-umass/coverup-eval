# file: docstring_parser/google.py:36-37
# asked: {"lines": [36, 37], "branches": []}
# gained: {"lines": [36, 37], "branches": []}

import pytest
from collections import namedtuple

def test_section_class():
    # Import the Section class from the module where it is defined
    from docstring_parser.google import Section

    # Create an instance of the Section class
    section_instance = Section(title="Test Title", key="test_key", type="test_type")

    # Assert that the instance is created correctly
    assert section_instance.title == "Test Title"
    assert section_instance.key == "test_key"
    assert section_instance.type == "test_type"

    # Assert that the docstring is correct
    assert Section.__doc__ == "A docstring section."
