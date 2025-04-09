# file: dataclasses_json/core.py:32-50
# asked: {"lines": [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}
# gained: {"lines": [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[35, 36], [35, 40], [36, 37], [36, 39], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 49]]}

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

class TestExtendedEncoder:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.encoder = _ExtendedEncoder()

    def test_collection_mapping(self):
        data = {1: 'a', 2: 'b'}
        result = self.encoder.default(data)
        assert result == {1: 'a', 2: 'b'}

    def test_collection_non_mapping(self):
        data = [1, 2, 3]
        result = self.encoder.default(data)
        assert result == [1, 2, 3]

    def test_datetime(self):
        dt = datetime(2020, 1, 1)
        result = self.encoder.default(dt)
        assert result == dt.timestamp()

    def test_uuid(self):
        uid = UUID('12345678123456781234567812345678')
        result = self.encoder.default(uid)
        assert result == str(uid)

    def test_enum(self):
        enum_val = SampleEnum.VALUE1
        result = self.encoder.default(enum_val)
        assert result == enum_val.value

    def test_decimal(self):
        dec = Decimal('10.5')
        result = self.encoder.default(dec)
        assert result == str(dec)

    def test_default(self):
        class CustomType:
            pass
        custom = CustomType()
        with pytest.raises(TypeError):
            self.encoder.default(custom)
