# file dataclasses_json/core.py:32-50
# lines [32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50]
# branches ['35->36', '35->40', '36->37', '36->39', '40->41', '40->42', '42->43', '42->44', '44->45', '44->46', '46->47', '46->49']

import json
from collections.abc import Collection, Mapping
from datetime import datetime
from enum import Enum
from decimal import Decimal
from uuid import UUID
import pytest

# Assuming the _isinstance_safe function is defined somewhere in the module
# If not, we need to mock or define it for the test
from dataclasses_json.core import _isinstance_safe

# Define a test class for the _ExtendedEncoder
class TestExtendedEncoder:
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    @pytest.fixture
    def encoder(self):
        from dataclasses_json.core import _ExtendedEncoder
        return _ExtendedEncoder()

    def test_encode_collection(self, encoder):
        collection = [1, 2, 3]
        assert encoder.default(collection) == collection

    def test_encode_mapping(self, encoder):
        mapping = {'a': 1, 'b': 2}
        assert encoder.default(mapping) == mapping

    def test_encode_datetime(self, encoder):
        dt = datetime(2020, 1, 1)
        assert encoder.default(dt) == dt.timestamp()

    def test_encode_uuid(self, encoder):
        uuid_obj = UUID('12345678123456781234567812345678')
        assert encoder.default(uuid_obj) == str(uuid_obj)

    def test_encode_enum(self, encoder):
        color = self.Color.RED
        assert encoder.default(color) == color.value

    def test_encode_decimal(self, encoder):
        decimal_obj = Decimal('10.5')
        assert encoder.default(decimal_obj) == str(decimal_obj)

    def test_encode_unsupported_type(self, encoder):
        class UnsupportedType:
            pass

        with pytest.raises(TypeError):
            encoder.default(UnsupportedType())

# The following code is not part of the test and should not be executed
# It is just a placeholder for the _isinstance_safe function
# If the function is not defined in the module, it should be mocked
def _isinstance_safe(obj, cls):
    return isinstance(obj, cls)
