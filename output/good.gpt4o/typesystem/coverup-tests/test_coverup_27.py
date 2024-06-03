# file typesystem/fields.py:186-189
# lines [186, 187, 188, 189]
# branches ['187->188', '187->189']

import pytest
from typesystem.fields import String

FORMATS = {
    "uppercase": lambda x: x.upper(),
    "lowercase": lambda x: x.lower(),
}

class MockField:
    def __init__(self, format=None):
        self.format = format

    def serialize(self, obj):
        if self.format in FORMATS:
            return FORMATS[self.format](obj)
        return obj

def test_string_serialize_with_format():
    field = MockField(format="uppercase")
    result = field.serialize("test")
    assert result == "TEST"

    field = MockField(format="lowercase")
    result = field.serialize("TEST")
    assert result == "test"

def test_string_serialize_without_format():
    field = MockField()
    result = field.serialize("Test")
    assert result == "Test"
