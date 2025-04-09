# file dataclasses_json/mm.py:227-275
# lines [233, 236, 237, 238, 239, 240, 242, 243, 244, 247, 249, 253, 256, 262, 265, 266, 267, 268]
# branches ['230->233', '235->236', '236->237', '236->242', '255->256', '261->262', '264->265']

import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json, DataClassJsonMixin
from dataclasses_json.mm import build_type
from marshmallow import fields
from enum import Enum
from typing import Union, NewType, Optional

# Define a NewType for testing __supertype__ branch
NewTypeInt = NewType('NewTypeInt', int)

# Define an Enum for testing the Enum branch
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Define a dataclass that does not inherit from DataClassJsonMixin for testing the warning branch
@dataclass
class NonJsonMixinDataclass:
    id: int

# Define a dataclass that inherits from DataClassJsonMixin for testing the Nested branch
@dataclass_json
@dataclass
class JsonMixinDataclass(DataClassJsonMixin):
    name: str

# Define a dataclass with various fields to cover all branches
@dataclass_json
@dataclass
class ComplexDataclass(DataClassJsonMixin):
    new_type_field: NewTypeInt
    enum_field: Color
    union_field: Union[int, str]
    optional_field: Optional[int]
    non_json_mixin_field: NonJsonMixinDataclass
    json_mixin_field: JsonMixinDataclass

def test_build_type_full_coverage(mocker):
    # Mock the warnings to assert they are called
    warn_mock = mocker.patch('dataclasses_json.mm.warnings.warn')

    # Test __supertype__ branch
    field = ComplexDataclass.__dataclass_fields__['new_type_field']
    build_type(NewTypeInt, {}, DataClassJsonMixin, field, ComplexDataclass)

    # Test Enum branch
    field = ComplexDataclass.__dataclass_fields__['enum_field']
    enum_field = build_type(Color, {}, DataClassJsonMixin, field, ComplexDataclass)
    assert isinstance(enum_field, fields.Field)

    # Test Union branch
    field = ComplexDataclass.__dataclass_fields__['union_field']
    union_field = build_type(Union[int, str], {}, DataClassJsonMixin, field, ComplexDataclass)
    assert isinstance(union_field, fields.Field)

    # Test Optional branch
    field = ComplexDataclass.__dataclass_fields__['optional_field']
    optional_field = build_type(Optional[int], {}, DataClassJsonMixin, field, ComplexDataclass)
    assert isinstance(optional_field, fields.Field)
    assert optional_field.allow_none is True

    # Test warning branch for a dataclass that does not inherit from DataClassJsonMixin
    field = ComplexDataclass.__dataclass_fields__['non_json_mixin_field']
    non_json_mixin_field = build_type(NonJsonMixinDataclass, {}, DataClassJsonMixin, field, ComplexDataclass)
    assert isinstance(non_json_mixin_field, fields.Field)
    warn_mock.assert_called()

    # Test Nested branch for a dataclass that inherits from DataClassJsonMixin
    field = ComplexDataclass.__dataclass_fields__['json_mixin_field']
    json_mixin_field = build_type(JsonMixinDataclass, {}, DataClassJsonMixin, field, ComplexDataclass)
    assert isinstance(json_mixin_field, fields.Nested)

    # Cleanup is not necessary as we are not modifying any global state
