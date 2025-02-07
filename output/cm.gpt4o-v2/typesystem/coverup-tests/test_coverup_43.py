# file: typesystem/fields.py:186-189
# asked: {"lines": [186, 187, 188, 189], "branches": [[187, 188], [187, 189]]}
# gained: {"lines": [186, 187, 188, 189], "branches": [[187, 188], [187, 189]]}

import pytest
import datetime
from typesystem.fields import String
from typesystem.formats import DateFormat, TimeFormat, DateTimeFormat, UUIDFormat

FORMATS = {
    'date': DateFormat(),
    'time': TimeFormat(),
    'datetime': DateTimeFormat(),
    'uuid': UUIDFormat()
}

def test_string_serialize_with_format():
    field = String(format='date')
    obj = datetime.date(2023, 10, 1)
    result = field.serialize(obj)
    assert result == FORMATS['date'].serialize(obj)

def test_string_serialize_without_format():
    field = String(format='nonexistent')
    obj = 'some string'
    result = field.serialize(obj)
    assert result == obj
