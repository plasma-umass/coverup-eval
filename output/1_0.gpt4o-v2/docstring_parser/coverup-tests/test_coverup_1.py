# file: docstring_parser/styles.py:8-12
# asked: {"lines": [8, 9, 10, 11, 12], "branches": []}
# gained: {"lines": [8, 9, 10, 11, 12], "branches": []}

import pytest
from docstring_parser.styles import Style

def test_style_enum():
    assert Style.rest.value == 1
    assert Style.google.value == 2
    assert Style.numpydoc.value == 3
    assert Style.auto.value == 255
