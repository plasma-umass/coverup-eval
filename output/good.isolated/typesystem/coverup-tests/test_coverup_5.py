# file typesystem/fields.py:661-674
# lines [661, 662, 663, 665, 666, 667, 668, 671, 672, 674]
# branches ['662->663', '662->665', '665->666', '665->671', '671->672', '671->674']

import pytest
from typesystem.fields import Array, Field

class MockSerializer(Field):
    def serialize(self, obj):
        return f"serialized_{obj}"

@pytest.fixture
def cleanup():
    # No cleanup needed for this test
    yield

def test_array_serialize_with_list_of_serializers(cleanup):
    serializers = [MockSerializer(), MockSerializer()]
    array_field = Array(items=serializers)
    input_data = [1, 2]
    expected_output = ['serialized_1', 'serialized_2']
    assert array_field.serialize(input_data) == expected_output

def test_array_serialize_with_single_serializer(cleanup):
    serializer = MockSerializer()
    array_field = Array(items=serializer)
    input_data = [1, 2, 3]
    expected_output = ['serialized_1', 'serialized_2', 'serialized_3']
    assert array_field.serialize(input_data) == expected_output

def test_array_serialize_with_none_items(cleanup):
    array_field = Array(items=None)
    input_data = [1, 2, 3]
    expected_output = [1, 2, 3]
    assert array_field.serialize(input_data) == expected_output

def test_array_serialize_with_none_obj(cleanup):
    array_field = Array(items=MockSerializer())
    input_data = None
    expected_output = None
    assert array_field.serialize(input_data) == expected_output
