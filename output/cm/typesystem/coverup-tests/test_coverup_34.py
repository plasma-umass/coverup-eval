# file typesystem/fields.py:677-679
# lines [677, 678, 679]
# branches []

import pytest
from typesystem.fields import Text

def test_text_initialization():
    text_field = Text()
    assert text_field.format == "text"
