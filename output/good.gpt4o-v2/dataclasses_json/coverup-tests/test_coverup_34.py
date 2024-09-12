# file: dataclasses_json/mm.py:227-275
# asked: {"lines": [233, 236, 237, 238, 239, 240, 242, 243, 244, 247, 249, 253, 256, 261, 262, 264, 265, 266, 267, 268, 270, 271, 273], "branches": [[230, 233], [235, 236], [236, 237], [236, 242], [255, 256], [258, 261], [261, 262], [261, 264], [264, 265], [264, 270]]}
# gained: {"lines": [236, 237, 238, 239, 240, 242, 243, 244, 247, 249, 253, 256, 261, 262, 264, 265, 266, 267, 268, 270, 271, 273], "branches": [[235, 236], [236, 237], [236, 242], [255, 256], [258, 261], [261, 262], [261, 264], [264, 265], [264, 270]]}

import pytest
from unittest.mock import Mock
from dataclasses import dataclass, field as dc_field
from enum import Enum
from marshmallow import fields
from marshmallow_enum import EnumField
from dataclasses_json.mm import build_type
from dataclasses_json.utils import _is_new_type, _issubclass_safe, _is_collection, _is_optional
from dataclasses_json.core import _is_supported_generic
from typing import List, Optional, Union

# Mock classes and functions
class MockEnum(Enum):
    A = 1
    B = 2

@dataclass
class MockDataclass:
    x: int

@dataclass
class MockDataclassJson:
    x: int

MockDataclassJson.schema = Mock(return_value=Mock())

class MockField:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

def test_build_type_new_type(monkeypatch):
    mock_type = Mock()
    mock_type.__supertype__ = int
    monkeypatch.setattr('dataclasses_json.utils._is_new_type', lambda x: True)
    result = build_type(mock_type, {}, None, MockField('test', int), MockDataclassJson)
    assert isinstance(result, fields.Field)

def test_build_type_dataclass(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._issubclass_safe', return_value=True)
    mocker.patch('dataclasses_json.core._is_supported_generic', return_value=True)
    mocker.patch('dataclasses_json.utils._is_collection', return_value=True)
    field = MockField('test', List[int])
    result = build_type(MockDataclassJson, {}, MockDataclassJson, field, MockDataclassJson)
    assert isinstance(result, fields.Nested)

def test_build_type_dataclass_warning(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._issubclass_safe', return_value=False)
    field = MockField('test', MockDataclass)
    with pytest.warns(UserWarning):
        result = build_type(MockDataclass, {}, MockDataclassJson, field, MockDataclassJson)
    assert isinstance(result, fields.Field)

def test_build_type_optional(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._is_optional', return_value=True)
    field = MockField('test', Optional[int])
    result = build_type(Optional[int], {}, MockDataclassJson, field, MockDataclassJson)
    assert result.allow_none is True

def test_build_type_enum(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._issubclass_safe', return_value=True)
    field = MockField('test', MockEnum)
    result = build_type(MockEnum, {}, MockDataclassJson, field, MockDataclassJson)
    assert isinstance(result, EnumField)

def test_build_type_union(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._issubclass_safe', return_value=False)
    mocker.patch('dataclasses_json.core._is_supported_generic', return_value=False)
    mocker.patch('dataclasses_json.utils._is_optional', return_value=False)
    mocker.patch('dataclasses_json.utils._is_collection', return_value=False)
    field = MockField('test', Union[int, str])
    result = build_type(Union[int, str], {}, MockDataclassJson, field, MockDataclassJson)
    assert isinstance(result, fields.Field)

def test_build_type_unknown_type(mocker):
    mocker.patch('dataclasses_json.utils._is_new_type', return_value=False)
    mocker.patch('dataclasses_json.utils._issubclass_safe', return_value=False)
    mocker.patch('dataclasses_json.core._is_supported_generic', return_value=False)
    mocker.patch('dataclasses_json.utils._is_optional', return_value=False)
    mocker.patch('dataclasses_json.utils._is_collection', return_value=False)
    field = MockField('test', complex)
    with pytest.warns(UserWarning):
        result = build_type(complex, {}, MockDataclassJson, field, MockDataclassJson)
    assert isinstance(result, fields.Field)
