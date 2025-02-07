# file: dataclasses_json/core.py:32-50
# asked: {"lines": [39, 49], "branches": [[36, 39], [46, 49]]}
# gained: {"lines": [39, 49], "branches": [[36, 39], [46, 49]]}

import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Collection, Mapping
from uuid import UUID
from dataclasses_json.utils import _isinstance_safe
from dataclasses_json.core import _ExtendedEncoder
import pytest

class CustomEnum(Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"

def test_extended_encoder_collection_not_mapping():
    encoder = _ExtendedEncoder()
    data = [1, 2, 3]
    result = encoder.default(data)
    assert result == data

def test_extended_encoder_default_case():
    encoder = _ExtendedEncoder()
    class CustomClass:
        pass
    data = CustomClass()
    with pytest.raises(TypeError):
        encoder.default(data)

def test_extended_encoder_decimal():
    encoder = _ExtendedEncoder()
    data = Decimal('10.5')
    result = encoder.default(data)
    assert result == '10.5'

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: monkeypatch or other setup steps
    yield
    # Teardown: clean up after tests
    # No specific teardown needed for these tests
