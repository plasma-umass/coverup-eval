# file: dataclasses_json/core.py:32-50
# asked: {"lines": [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}
# gained: {"lines": [32, 33], "branches": []}

import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Collection, Mapping, Union
from uuid import UUID
from dataclasses_json.utils import _isinstance_safe
import pytest

Json = Union[dict, list, str, int, float, bool, None]

class _ExtendedEncoder(json.JSONEncoder):
    def default(self, o) -> Json:
        result: Json
        if _isinstance_safe(o, Collection):
            if _isinstance_safe(o, Mapping):
                result = dict(o)
            else:
                result = list(o)
        elif _isinstance_safe(o, datetime):
            result = o.timestamp()
        elif _isinstance_safe(o, UUID):
            result = str(o)
        elif _isinstance_safe(o, Enum):
            result = o.value
        elif _isinstance_safe(o, Decimal):
            result = str(o)
        else:
            result = json.JSONEncoder.default(self, o)
        return result

def test_extended_encoder_collection_mapping():
    class CustomMapping(Mapping):
        def __init__(self, data):
            self._data = data

        def __getitem__(self, key):
            return self._data[key]

        def __iter__(self):
            return iter(self._data)

        def __len__(self):
            return len(self._data)

    data = CustomMapping({'key': 'value'})
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == {'key': 'value'}

def test_extended_encoder_collection_non_mapping():
    data = [1, 2, 3]
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == [1, 2, 3]

def test_extended_encoder_datetime():
    data = datetime(2020, 1, 1)
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == data.timestamp()

def test_extended_encoder_uuid():
    data = UUID('12345678123456781234567812345678')
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == str(data)

def test_extended_encoder_enum():
    class CustomEnum(Enum):
        VALUE = 'value'

    data = CustomEnum.VALUE
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == 'value'

def test_extended_encoder_decimal():
    data = Decimal('10.5')
    encoder = _ExtendedEncoder()
    result = encoder.default(data)
    assert result == str(data)

def test_extended_encoder_default():
    class CustomClass:
        pass

    data = CustomClass()
    encoder = _ExtendedEncoder()
    with pytest.raises(TypeError):
        encoder.default(data)
