# file: typesystem/fields.py:402-444
# asked: {"lines": [402, 405, 406, 407, 408, 409, 410, 411, 414, 416, 417, 418, 420, 421, 422, 424, 425, 427, 428, 429, 430, 431, 432, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444], "branches": [[416, 417], [416, 420]]}
# gained: {"lines": [402, 405, 406, 407, 408, 409, 410, 411, 414, 416, 420, 421, 422, 424, 425, 427, 428, 429, 430, 431, 432, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444], "branches": [[416, 420]]}

import pytest
from typesystem.fields import Field, Object

class MockField(Field):
    pass

@pytest.fixture
def mock_field():
    return MockField()

def test_object_init_with_properties(mock_field):
    obj = Object(properties={"key": mock_field})
    assert obj.properties == {"key": mock_field}
    assert obj.additional_properties is True

def test_object_init_with_pattern_properties(mock_field):
    obj = Object(pattern_properties={"pattern": mock_field})
    assert obj.pattern_properties == {"pattern": mock_field}

def test_object_init_with_additional_properties(mock_field):
    obj = Object(additional_properties=mock_field)
    assert obj.additional_properties == mock_field

def test_object_init_with_property_names(mock_field):
    obj = Object(property_names=mock_field)
    assert obj.property_names == mock_field

def test_object_init_with_min_properties():
    obj = Object(min_properties=1)
    assert obj.min_properties == 1

def test_object_init_with_max_properties():
    obj = Object(max_properties=10)
    assert obj.max_properties == 10

def test_object_init_with_required():
    obj = Object(required=["key1", "key2"])
    assert obj.required == ["key1", "key2"]

def test_object_init_with_all_params(mock_field):
    obj = Object(
        properties={"key": mock_field},
        pattern_properties={"pattern": mock_field},
        additional_properties=mock_field,
        property_names=mock_field,
        min_properties=1,
        max_properties=10,
        required=["key1", "key2"]
    )
    assert obj.properties == {"key": mock_field}
    assert obj.pattern_properties == {"pattern": mock_field}
    assert obj.additional_properties == mock_field
    assert obj.property_names == mock_field
    assert obj.min_properties == 1
    assert obj.max_properties == 10
    assert obj.required == ["key1", "key2"]

def test_object_init_with_invalid_properties():
    with pytest.raises(AssertionError):
        Object(properties={"key": "not_a_field"})

def test_object_init_with_invalid_pattern_properties():
    with pytest.raises(AssertionError):
        Object(pattern_properties={"pattern": "not_a_field"})

def test_object_init_with_invalid_additional_properties():
    with pytest.raises(AssertionError):
        Object(additional_properties="not_a_field")

def test_object_init_with_invalid_min_properties():
    with pytest.raises(AssertionError):
        Object(min_properties="not_an_int")

def test_object_init_with_invalid_max_properties():
    with pytest.raises(AssertionError):
        Object(max_properties="not_an_int")

def test_object_init_with_invalid_required():
    with pytest.raises(AssertionError):
        Object(required=["key1", 2])
