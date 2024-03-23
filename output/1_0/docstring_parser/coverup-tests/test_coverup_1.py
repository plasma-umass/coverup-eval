# file docstring_parser/styles.py:8-12
# lines [8, 9, 10, 11, 12]
# branches []

import pytest
from docstring_parser.styles import Style

def test_style_enum():
    assert Style.rest == Style(1)
    assert Style.google == Style(2)
    assert Style.numpydoc == Style(3)
    assert Style.auto == Style(255)

    # Test that invalid enum raises ValueError
    with pytest.raises(ValueError):
        Style(4)

    # Test that all enum members are covered
    assert set(Style) == {Style.rest, Style.google, Style.numpydoc, Style.auto}
