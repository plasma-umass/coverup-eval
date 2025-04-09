# file: typesystem/fields.py:186-189
# asked: {"lines": [186, 187, 188, 189], "branches": [[187, 188], [187, 189]]}
# gained: {"lines": [186, 187, 188, 189], "branches": [[187, 188], [187, 189]]}

import pytest
from typesystem.fields import String
from typesystem.formats import DateFormat, TimeFormat, DateTimeFormat, UUIDFormat
import datetime

def test_string_serialize_with_format():
    string_field = String(format='date')
    obj = datetime.date(2023, 10, 5)
    result = string_field.serialize(obj)
    assert result == DateFormat().serialize(obj)

def test_string_serialize_without_format():
    string_field = String()
    obj = 'some string'
    result = string_field.serialize(obj)
    assert result == obj
