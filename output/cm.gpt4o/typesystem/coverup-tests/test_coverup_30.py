# file typesystem/fields.py:446-547
# lines [446, 447, 448, 449, 450, 451, 452, 454, 455, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 471, 472, 473, 474, 476, 477, 478, 479, 482, 483, 484, 485, 486, 489, 490, 491, 492, 493, 494, 495, 496, 497, 499, 502, 503, 504, 505, 506, 507, 508, 510, 511, 513, 516, 517, 518, 521, 522, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 542, 544, 545, 547]
# branches ['447->448', '447->449', '449->450', '449->451', '451->452', '451->454', '458->459', '458->471', '459->460', '459->463', '463->458', '463->464', '465->458', '465->466', '471->472', '471->477', '472->473', '472->477', '473->474', '473->476', '477->478', '477->482', '478->479', '478->482', '482->483', '482->489', '483->482', '483->484', '489->490', '489->502', '490->491', '490->494', '491->492', '491->493', '496->497', '496->499', '502->503', '502->516', '503->504', '503->516', '504->503', '504->505', '505->504', '505->506', '510->511', '510->513', '525->526', '525->528', '526->527', '526->544', '528->529', '528->533', '529->530', '529->544', '533->534', '533->544', '536->537', '536->544', '539->540', '539->542', '544->545', '544->547']

import pytest
from typesystem.fields import Object, Field, Message, ValidationError
import typing
import re

class MockField(Field):
    def __init__(self, default=None, allow_null=False):
        self._default = default
        self.allow_null = allow_null

    def has_default(self):
        return self._default is not None

    def get_default_value(self):
        return self._default

    def validate_or_error(self, value, strict=False):
        if isinstance(value, str):
            return value, None
        return None, ValidationError(messages=[Message(text="invalid", code="invalid")])

@pytest.fixture
def object_field():
    return Object(
        properties={
            "name": MockField(),
            "age": MockField(),
        },
        required=["name"],
        min_properties=1,
        max_properties=3,
        additional_properties=False,
        allow_null=False,
    )

def test_object_field_validate(object_field):
    # Test valid input
    value = {"name": "John", "age": "30"}
    validated = object_field.validate(value)
    assert validated == value

    # Test missing required property
    value = {"age": "30"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "required"

    # Test invalid type for property
    value = {"name": 123, "age": "30"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "invalid"

    # Test min_properties
    value = {}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "empty"

    # Test max_properties
    value = {"name": "John", "age": "30", "extra": "value", "extra2": "value2"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "max_properties"

    # Test additional_properties
    value = {"name": "John", "age": "30", "extra": "value"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "invalid_property"

    # Test pattern_properties
    object_field.pattern_properties = {r"^extra_": MockField()}
    value = {"name": "John", "age": "30", "extra_1": "value"}
    validated = object_field.validate(value)
    assert validated == value

    # Test invalid key type
    value = {123: "invalid_key", "name": "John"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "invalid_key"

    # Test property_names validation
    object_field.property_names = MockField()
    value = {"invalid_property_name": "value", "name": "John"}
    with pytest.raises(ValidationError) as excinfo:
        object_field.validate(value)
    assert excinfo.value.messages()[0].code == "invalid_property"
