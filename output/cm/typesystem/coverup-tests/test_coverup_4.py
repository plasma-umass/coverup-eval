# file typesystem/fields.py:402-444
# lines [402, 405, 406, 407, 408, 409, 410, 411, 414, 416, 417, 418, 420, 421, 422, 424, 425, 427, 428, 429, 430, 431, 432, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444]
# branches ['416->417', '416->420']

import pytest
from typesystem.fields import Field, Object

class MockField(Field):
    pass

def test_object_field_initialization():
    # Test the initialization of the Object field with various parameters
    properties = {'prop1': MockField()}
    pattern_properties = {'^S': MockField()}
    additional_properties = MockField()
    property_names = MockField()
    min_properties = 1
    max_properties = 5
    required = ['prop1']

    obj_field = Object(
        properties=properties,
        pattern_properties=pattern_properties,
        additional_properties=additional_properties,
        property_names=property_names,
        min_properties=min_properties,
        max_properties=max_properties,
        required=required
    )

    assert obj_field.properties == properties
    assert obj_field.pattern_properties == pattern_properties
    assert obj_field.additional_properties == additional_properties
    assert obj_field.property_names == property_names
    assert obj_field.min_properties == min_properties
    assert obj_field.max_properties == max_properties
    assert obj_field.required == required

def test_object_field_with_properties_as_field():
    # Test the case where 'properties' is provided as a Field instance
    properties_as_field = MockField()
    obj_field = Object(properties=properties_as_field)

    assert obj_field.additional_properties == properties_as_field
    assert obj_field.properties == {}

def test_object_field_with_none_values():
    # Test the case where None values are provided for properties and pattern_properties
    obj_field = Object(properties=None, pattern_properties=None)

    assert obj_field.properties == {}
    assert obj_field.pattern_properties == {}

def test_object_field_with_required_as_tuple():
    # Test the case where 'required' is provided as a tuple
    required_as_tuple = ('prop1', 'prop2')
    obj_field = Object(required=required_as_tuple)

    assert obj_field.required == list(required_as_tuple)

def test_object_field_with_no_required():
    # Test the case where 'required' is not provided
    obj_field = Object()

    assert obj_field.required == []

def test_object_field_with_invalid_parameters():
    # Test the case where invalid parameters are provided
    with pytest.raises(AssertionError):
        Object(properties={'prop1': 'not_a_field'})
    with pytest.raises(AssertionError):
        Object(pattern_properties={'^S': 'not_a_field'})
    with pytest.raises(AssertionError):
        Object(additional_properties='not_a_field_or_bool')
    with pytest.raises(AssertionError):
        Object(min_properties='not_an_int')
    with pytest.raises(AssertionError):
        Object(max_properties='not_an_int')
    with pytest.raises(AssertionError):
        Object(required=['prop1', 123])
