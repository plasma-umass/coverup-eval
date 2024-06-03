# file typesystem/fields.py:687-689
# lines [687, 688, 689]
# branches []

import pytest
import typing
from typesystem.fields import String

class Time(String):
    def __init__(self, **kwargs: typing.Any) -> None:
        super().__init__(format="time", **kwargs)

def test_time_field_initialization():
    time_field = Time()
    assert time_field.format == "time"
    assert isinstance(time_field, String)
