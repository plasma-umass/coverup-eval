# file: typesystem/formats.py:106-154
# asked: {"lines": [106, 107, 108, 109, 112, 113, 115, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 122], [121, 124], [125, 126], [125, 127], [127, 128], [127, 135], [131, 132], [131, 133], [144, 145], [144, 147], [151, 152], [151, 154]]}
# gained: {"lines": [106, 107, 108, 109, 112, 113, 115, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 133, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 122], [121, 124], [125, 126], [125, 127], [127, 128], [127, 135], [131, 133], [144, 145], [144, 147], [151, 152], [151, 154]]}

import pytest
import datetime
from typesystem.formats import DateTimeFormat
from typesystem import ValidationError

def test_is_native_type():
    format = DateTimeFormat()
    assert format.is_native_type(datetime.datetime.now()) is True
    assert format.is_native_type("2023-10-05T14:48:00") is False

def test_validate():
    format = DateTimeFormat()
    
    # Valid datetime with microseconds and UTC timezone
    dt_str = "2023-10-05T14:48:00.123456Z"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 5, 14, 48, 0, 123456, tzinfo=datetime.timezone.utc)
    
    # Valid datetime with timezone offset
    dt_str = "2023-10-05T14:48:00+02:00"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 5, 14, 48, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    
    # Valid datetime without timezone
    dt_str = "2023-10-05T14:48:00"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 5, 14, 48, 0)
    
    # Invalid datetime format
    with pytest.raises(ValidationError, match="Must be a valid datetime format."):
        format.validate("invalid-datetime")
    
    # Invalid datetime value
    with pytest.raises(ValidationError, match="Must be a real datetime."):
        format.validate("2023-13-05T14:48:00")  # Invalid month

def test_serialize():
    format = DateTimeFormat()
    
    # Serialize None
    assert format.serialize(None) is None
    
    # Serialize datetime with UTC timezone
    dt = datetime.datetime(2023, 10, 5, 14, 48, 0, 123456, tzinfo=datetime.timezone.utc)
    assert format.serialize(dt) == "2023-10-05T14:48:00.123456Z"
    
    # Serialize datetime with timezone offset
    dt = datetime.datetime(2023, 10, 5, 14, 48, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    assert format.serialize(dt) == "2023-10-05T14:48:00+02:00"
    
    # Serialize datetime without timezone
    dt = datetime.datetime(2023, 10, 5, 14, 48, 0)
    assert format.serialize(dt) == "2023-10-05T14:48:00"
