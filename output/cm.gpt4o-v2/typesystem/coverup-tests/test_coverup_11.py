# file: typesystem/fields.py:402-444
# asked: {"lines": [402, 405, 406, 407, 408, 409, 410, 411, 414, 416, 417, 418, 420, 421, 422, 424, 425, 427, 428, 429, 430, 431, 432, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444], "branches": [[416, 417], [416, 420]]}
# gained: {"lines": [402, 405, 406, 407, 408, 409, 410, 411, 414, 416, 417, 418, 420, 421, 422, 424, 425, 427, 428, 429, 430, 431, 432, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444], "branches": [[416, 417], [416, 420]]}

import pytest
from typesystem.fields import Object, Field

class DummyField(Field):
    pass

def test_object_init_with_all_params():
    properties = {"prop1": DummyField(), "prop2": DummyField()}
    pattern_properties = {"pattern1": DummyField(), "pattern2": DummyField()}
    additional_properties = DummyField()
    property_names = DummyField()
    min_properties = 1
    max_properties = 5
    required = ["prop1", "prop2"]

    obj = Object(
        properties=properties,
        pattern_properties=pattern_properties,
        additional_properties=additional_properties,
        property_names=property_names,
        min_properties=min_properties,
        max_properties=max_properties,
        required=required,
    )

    assert obj.properties == properties
    assert obj.pattern_properties == pattern_properties
    assert obj.additional_properties == additional_properties
    assert obj.property_names == property_names
    assert obj.min_properties == min_properties
    assert obj.max_properties == max_properties
    assert obj.required == required

def test_object_init_with_field_as_properties():
    field_instance = DummyField()
    obj = Object(properties=field_instance)

    assert obj.properties == {}
    assert obj.additional_properties == field_instance

def test_object_init_with_none_params():
    obj = Object()

    assert obj.properties == {}
    assert obj.pattern_properties == {}
    assert obj.additional_properties is True
    assert obj.property_names is None
    assert obj.min_properties is None
    assert obj.max_properties is None
    assert obj.required == []

def test_object_init_with_invalid_properties():
    with pytest.raises(AssertionError):
        Object(properties={"prop1": "not_a_field"})

def test_object_init_with_invalid_pattern_properties():
    with pytest.raises(AssertionError):
        Object(pattern_properties={"pattern1": "not_a_field"})

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
        Object(required=["prop1", 2])
