# file typesystem/fields.py:677-679
# lines [677, 678, 679]
# branches []

import pytest
import typing
from typesystem.fields import String

class Text(String):
    def __init__(self, **kwargs: typing.Any) -> None:
        super().__init__(format="text", **kwargs)

def test_text_field_initialization():
    text_field = Text(max_length=100, min_length=10)
    
    assert text_field.format == "text"
    assert text_field.max_length == 100
    assert text_field.min_length == 10
