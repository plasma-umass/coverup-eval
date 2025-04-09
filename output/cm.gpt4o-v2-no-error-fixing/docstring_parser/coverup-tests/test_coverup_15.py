# file: docstring_parser/google.py:23-33
# asked: {"lines": [23, 24, 26, 27, 29, 30, 32, 33], "branches": []}
# gained: {"lines": [23, 24, 26, 27, 29, 30, 32, 33], "branches": []}

import pytest
from docstring_parser.google import SectionType

def test_section_type_enum():
    assert SectionType.SINGULAR == 0
    assert SectionType.SINGULAR.name == "SINGULAR"
    assert SectionType.SINGULAR.value == 0

    assert SectionType.MULTIPLE == 1
    assert SectionType.MULTIPLE.name == "MULTIPLE"
    assert SectionType.MULTIPLE.value == 1

    assert SectionType.SINGULAR_OR_MULTIPLE == 2
    assert SectionType.SINGULAR_OR_MULTIPLE.name == "SINGULAR_OR_MULTIPLE"
    assert SectionType.SINGULAR_OR_MULTIPLE.value == 2
