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

def test_object_initialization_with_defaults():
    obj = Object()
    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_initialization_with_properties(mock_field):
    properties = {"prop1": mock_field}
    obj = Object(properties=properties)
    assert obj.properties == properties
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_initialization_with_pattern_properties(mock_field):
    pattern_properties = {"pattern1": mock_field}
    obj = Object(pattern_properties=pattern_properties)
    assert obj.properties == {}
    assert obj.pattern_properties == pattern_properties
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_initialization_with_additional_properties(mock_field):
    obj = Object(additional_properties=mock_field)
    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties == mock_field
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_initialization_with_property_names(mock_field):
    obj = Object(property_names=mock_field)
    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names == mock_field
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_initialization_with_min_max_properties():
    obj = Object(min_properties=1, max_properties=5)
    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties == 1
    assert obj.max_properties == 5
    assert obj.required == []

def test_object_initialization_with_required():
    required = ["prop1", "prop2"]
    obj = Object(required=required)
    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == required

def test_object_initialization_with_all_parameters(mock_field):
    properties = {"prop1": mock_field}
    pattern_properties = {"pattern1": mock_field}
    required = ["prop1"]
    obj = Object(
        properties=properties,
        pattern_properties=pattern_properties,
        additional_properties=mock_field,
        property_names=mock_field,
        min_properties=1,
        max_properties=5,
        required=required,
    )
    assert obj.properties == properties
    assert obj.pattern_properties == pattern_properties
    assert obj.additional_properties == mock_field
    assert obj.property_names == mock_field
    assert obj.min_properties == 1
    assert obj.max_properties == 5
    assert obj.required == required
