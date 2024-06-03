# file dataclasses_json/core.py:32-50
# lines [37, 40, 41, 42, 43, 44, 45, 46, 47, 49]
# branches ['35->40', '36->37', '40->41', '40->42', '42->43', '42->44', '44->45', '44->46', '46->47', '46->49']

import pytest
from unittest.mock import patch
import json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
from collections.abc import Collection, Mapping

# Assuming _isinstance_safe is a function in the same module
from dataclasses_json.core import _isinstance_safe

class TestExtendedEncoder:
    class SampleEnum(Enum):
        VALUE1 = 1
        VALUE2 = 2

    @pytest.fixture
    def encoder(self):
        from dataclasses_json.core import _ExtendedEncoder
        return _ExtendedEncoder()

    def test_collection_mapping(self, encoder):
        data = {'key': 'value'}
        result = encoder.default(data)
        assert result == {'key': 'value'}

    def test_collection_non_mapping(self, encoder):
        data = [1, 2, 3]
        result = encoder.default(data)
        assert result == [1, 2, 3]

    def test_datetime(self, encoder):
        dt = datetime(2020, 1, 1)
        result = encoder.default(dt)
        assert result == dt.timestamp()

    def test_uuid(self, encoder):
        uid = UUID('12345678123456781234567812345678')
        result = encoder.default(uid)
        assert result == str(uid)

    def test_enum(self, encoder):
        enum_value = self.SampleEnum.VALUE1
        result = encoder.default(enum_value)
        assert result == enum_value.value

    def test_decimal(self, encoder):
        dec = Decimal('10.5')
        result = encoder.default(dec)
        assert result == str(dec)

    def test_default(self, encoder):
        class CustomObject:
            pass

        obj = CustomObject()
        with patch.object(json.JSONEncoder, 'default', return_value='default') as mock_default:
            result = encoder.default(obj)
            mock_default.assert_called_once_with(encoder, obj)
            assert result == 'default'
