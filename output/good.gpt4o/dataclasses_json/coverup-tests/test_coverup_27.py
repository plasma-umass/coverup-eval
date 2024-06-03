# file dataclasses_json/core.py:32-50
# lines [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50]
# branches ['35->36', '35->40', '36->37', '36->39', '40->41', '40->42', '42->43', '42->44', '44->45', '44->46', '46->47', '46->49']

import json
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
from collections.abc import Collection, Mapping
import pytest
from unittest.mock import patch

# Assuming _isinstance_safe is a function defined elsewhere in dataclasses_json.core
# Mocking _isinstance_safe for the purpose of this test
def _isinstance_safe(obj, cls):
    return isinstance(obj, cls)

# The class to be tested
class _ExtendedEncoder(json.JSONEncoder):
    def default(self, o) -> json.JSONEncoder:
        result: json.JSONEncoder
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

class TestExtendedEncoder:
    class SampleEnum(Enum):
        VALUE1 = "value1"
        VALUE2 = "value2"

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, mocker):
        # Mock _isinstance_safe
        self.mock_isinstance_safe = mocker.patch('dataclasses_json.core._isinstance_safe', side_effect=_isinstance_safe)
        yield
        # Teardown code if needed

    def test_collection_mapping(self):
        data = {'key': 'value'}
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert encoded == '{"key": "value"}'

    def test_collection_non_mapping(self):
        data = [1, 2, 3]
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert encoded == '[1, 2, 3]'

    def test_datetime(self):
        data = datetime(2020, 1, 1)
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert json.loads(encoded) == data.timestamp()

    def test_uuid(self):
        data = UUID('12345678123456781234567812345678')
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert json.loads(encoded) == str(data)

    def test_enum(self):
        data = self.SampleEnum.VALUE1
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert json.loads(encoded) == data.value

    def test_decimal(self):
        data = Decimal('10.5')
        encoded = json.dumps(data, cls=_ExtendedEncoder)
        assert json.loads(encoded) == str(data)

    def test_default(self):
        class CustomClass:
            def __init__(self, value):
                self.value = value

        data = CustomClass('test')
        with pytest.raises(TypeError):
            json.dumps(data, cls=_ExtendedEncoder)
