# file docstring_parser/google.py:23-33
# lines [23, 24, 26, 27, 29, 30, 32, 33]
# branches []

import pytest
from docstring_parser.google import SectionType

def test_section_type_enum():
    assert SectionType.SINGULAR == 0
    assert SectionType.MULTIPLE == 1
    assert SectionType.SINGULAR_OR_MULTIPLE == 2

    # Check the enum names
    assert SectionType(0).name == "SINGULAR"
    assert SectionType(1).name == "MULTIPLE"
    assert SectionType(2).name == "SINGULAR_OR_MULTIPLE"

    # Check the enum values
    assert SectionType(0).value == 0
    assert SectionType(1).value == 1
    assert SectionType(2).value == 2

    # Check if all enum members are covered
    assert set(SectionType) == {SectionType.SINGULAR, SectionType.MULTIPLE, SectionType.SINGULAR_OR_MULTIPLE}
