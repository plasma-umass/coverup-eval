# file: dataclasses_json/core.py:32-50
# asked: {"lines": [35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}
# gained: {"lines": [35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 50], "branches": [[35, 36], [35, 40], [36, 37], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47]]}

import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Collection, Mapping
from uuid import UUID
from dataclasses_json.utils import _isinstance_safe
from dataclasses_json.core import _ExtendedEncoder
import pytest

class SampleEnum(Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"

class CustomMapping(Mapping):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __iter__(self):
        return iter(self.__dict__)
    def __len__(self):
        return len(self.__dict__)
    def __getitem__(self, key):
        return self.__dict__[key]

def test_extended_encoder_collection_mapping():
    obj = CustomMapping(a=1, b=2)
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == '{"a": 1, "b": 2}'

def test_extended_encoder_collection():
    obj = [1, 2, 3]
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == '[1, 2, 3]'

def test_extended_encoder_datetime():
    obj = datetime(2020, 1, 1)
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == str(obj.timestamp())

def test_extended_encoder_uuid():
    obj = UUID('12345678123456781234567812345678')
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == '"12345678-1234-5678-1234-567812345678"'

def test_extended_encoder_enum():
    obj = SampleEnum.VALUE1
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == '"value1"'

def test_extended_encoder_decimal():
    obj = Decimal('10.5')
    encoded = json.dumps(obj, cls=_ExtendedEncoder)
    assert encoded == '"10.5"'

def test_extended_encoder_default():
    class CustomObject:
        def __init__(self, value):
            self.value = value

        def to_json(self):
            return {"value": self.value}

    obj = CustomObject(10)
    encoded = json.dumps(obj.to_json(), cls=_ExtendedEncoder)
    assert '"value": 10' in encoded
