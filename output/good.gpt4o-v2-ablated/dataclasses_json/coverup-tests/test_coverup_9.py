# file: dataclasses_json/core.py:32-50
# asked: {"lines": [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}
# gained: {"lines": [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}

import json
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
from collections.abc import Collection, Mapping
import pytest
from dataclasses_json.core import _ExtendedEncoder

class TestEnum(Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"

class TestMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

class TestCollection(Collection):
    def __init__(self, data):
        self._data = data

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

@pytest.fixture
def setup():
    return _ExtendedEncoder()

def test_encode_mapping(setup):
    data = TestMapping({"key": "value"})
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == '{"key": "value"}'

def test_encode_collection(setup):
    data = TestCollection([1, 2, 3])
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == '[1, 2, 3]'

def test_encode_datetime(setup):
    data = datetime(2020, 1, 1)
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == str(data.timestamp())

def test_encode_uuid(setup):
    data = UUID("12345678123456781234567812345678")
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == '"12345678-1234-5678-1234-567812345678"'

def test_encode_enum(setup):
    data = TestEnum.VALUE1
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == '"value1"'

def test_encode_decimal(setup):
    data = Decimal("10.5")
    result = json.dumps(data, cls=_ExtendedEncoder)
    assert result == '"10.5"'

def test_encode_default(setup):
    class CustomType:
        pass

    data = CustomType()
    with pytest.raises(TypeError):
        json.dumps(data, cls=_ExtendedEncoder)
