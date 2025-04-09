# file: dataclasses_json/core.py:234-238
# asked: {"lines": [235, 236, 237, 238], "branches": []}
# gained: {"lines": [235, 236, 237, 238], "branches": []}

import pytest
from unittest.mock import patch
from enum import Enum
from typing import List, Optional, Union
from dataclasses_json.core import _is_supported_generic

class DummyEnum(Enum):
    VALUE1 = 1
    VALUE2 = 2

def test_is_supported_generic_with_collection():
    assert _is_supported_generic(List[int]) is True

def test_is_supported_generic_with_optional():
    assert _is_supported_generic(Optional[int]) is True

def test_is_supported_generic_with_union():
    assert _is_supported_generic(Union[int, str]) is True

def test_is_supported_generic_with_enum():
    assert _is_supported_generic(DummyEnum) is True

def test_is_supported_generic_with_str():
    assert _is_supported_generic(str) is False

def test_is_supported_generic_with_int():
    assert _is_supported_generic(int) is False
