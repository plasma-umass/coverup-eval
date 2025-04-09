# file: typesystem/fields.py:697-733
# asked: {"lines": [697, 698, 700, 701, 703, 704, 705, 707, 708, 709, 710, 711, 713, 714, 715, 716, 717, 721, 722, 723, 724, 725, 727, 729, 732, 733], "branches": [[704, 0], [704, 705], [708, 709], [708, 710], [710, 711], [710, 713], [714, 715], [714, 729], [716, 717], [716, 721], [722, 714], [722, 727], [729, 732], [729, 733]]}
# gained: {"lines": [697, 698, 700, 701, 703, 704, 705, 707, 708, 709, 710, 711, 713, 714, 715, 716, 717, 721, 722, 723, 724, 725, 727, 729, 732, 733], "branches": [[704, 0], [704, 705], [708, 709], [708, 710], [710, 711], [710, 713], [714, 715], [714, 729], [716, 717], [716, 721], [722, 714], [722, 727], [729, 732], [729, 733]]}

import pytest
from unittest.mock import Mock

from typesystem.fields import Union, Field

class MockField(Field):
    def __init__(self, allow_null=False, validate_return=None, validate_error=None):
        self.allow_null = allow_null
        self._validate_return = validate_return
        self._validate_error = validate_error

    def validate_or_error(self, value, strict=False):
        return self._validate_return, self._validate_error

class MockValidationError(Exception):
    def messages(self):
        return [Mock(code="non_type_error", index=None)]

def test_union_init():
    field1 = MockField(allow_null=False)
    field2 = MockField(allow_null=True)
    union_field = Union(any_of=[field1, field2])
    assert union_field.allow_null is True

    field3 = MockField(allow_null=False)
    union_field = Union(any_of=[field1, field3])
    assert union_field.allow_null is False

def test_union_validate_none_with_allow_null():
    field = MockField(allow_null=True)
    union_field = Union(any_of=[field])
    assert union_field.validate(None) is None

def test_union_validate_none_without_allow_null():
    field = MockField(allow_null=False)
    union_field = Union(any_of=[field])
    with pytest.raises(Exception) as excinfo:
        union_field.validate(None)
    assert str(excinfo.value) == "May not be null."

def test_union_validate_success():
    field = MockField(validate_return="validated_value")
    union_field = Union(any_of=[field])
    assert union_field.validate("some_value") == "validated_value"

def test_union_validate_type_error():
    error_mock = Mock()
    error_mock.messages.return_value = [Mock(code="type", index=None)]
    field = MockField(validate_error=error_mock)
    union_field = Union(any_of=[field])
    with pytest.raises(Exception) as excinfo:
        union_field.validate("some_value")
    assert str(excinfo.value) == "Did not match any valid type."

def test_union_validate_non_type_error():
    error_mock = MockValidationError()
    field = MockField(validate_error=error_mock)
    union_field = Union(any_of=[field])
    with pytest.raises(MockValidationError) as excinfo:
        union_field.validate("some_value")
    assert excinfo.value == error_mock

def test_union_validate_multiple_non_type_errors():
    error_mock1 = Mock()
    error_mock1.messages.return_value = [Mock(code="non_type_error_1", index=None)]
    error_mock2 = Mock()
    error_mock2.messages.return_value = [Mock(code="non_type_error_2", index=None)]
    field1 = MockField(validate_error=error_mock1)
    field2 = MockField(validate_error=error_mock2)
    union_field = Union(any_of=[field1, field2])
    with pytest.raises(Exception) as excinfo:
        union_field.validate("some_value")
    assert str(excinfo.value) == "Did not match any valid type."
