# file: docstring_parser/numpydoc.py:201-204
# asked: {"lines": [201, 202, 204], "branches": []}
# gained: {"lines": [201, 202, 204], "branches": []}

import pytest
from docstring_parser.numpydoc import YieldsSection

def test_yields_section_is_generator():
    assert YieldsSection.is_generator == True
