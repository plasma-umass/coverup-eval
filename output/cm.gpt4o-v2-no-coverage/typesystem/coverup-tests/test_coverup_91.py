# file: typesystem/fields.py:602-659
# asked: {"lines": [603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 615, 616, 617, 618, 619, 620, 621, 624, 625, 626, 627, 629, 630, 631, 632, 633, 634, 635, 636, 637, 639, 640, 642, 643, 644, 646, 648, 649, 650, 651, 652, 654, 656, 657, 659], "branches": [[603, 604], [603, 605], [605, 606], [605, 607], [607, 608], [607, 610], [610, 615], [610, 616], [616, 617], [616, 620], [617, 618], [617, 619], [620, 621], [620, 624], [626, 627], [626, 629], [629, 630], [629, 656], [631, 632], [631, 636], [632, 633], [632, 634], [634, 635], [634, 639], [636, 637], [636, 639], [639, 640], [639, 642], [643, 644], [643, 646], [648, 629], [648, 649], [649, 650], [649, 654], [656, 657], [656, 659]]}
# gained: {"lines": [603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 615, 616, 617, 618, 619, 620, 621, 624, 625, 626, 627, 629, 630, 631, 632, 633, 634, 635, 636, 637, 639, 640, 642, 643, 644, 646, 648, 649, 650, 651, 652, 654, 656, 657, 659], "branches": [[603, 604], [603, 605], [605, 606], [605, 607], [607, 608], [607, 610], [610, 615], [610, 616], [616, 617], [616, 620], [617, 618], [617, 619], [620, 621], [620, 624], [626, 627], [626, 629], [629, 630], [629, 656], [631, 632], [631, 636], [632, 633], [632, 634], [634, 635], [636, 637], [636, 639], [639, 640], [639, 642], [643, 644], [643, 646], [648, 629], [648, 649], [649, 650], [649, 654], [656, 657], [656, 659]]}

import pytest
from typesystem.fields import Array, Field
from typesystem.base import ValidationError, Message

class DummyField(Field):
    def validate_or_error(self, value, strict=False):
        if isinstance(value, int):
            return value, None
        return None, ValidationError(messages=[Message(text="Invalid type", code="type")])

def test_array_validate_allow_null():
    array_field = Array(allow_null=True)
    assert array_field.validate(None) is None

def test_array_validate_null():
    array_field = Array(allow_null=False)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate(None)
    assert exc_info.value.messages()[0].text == "May not be null."

def test_array_validate_type():
    array_field = Array()
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate("not a list")
    assert exc_info.value.messages()[0].text == "Must be an array."

def test_array_validate_exact_items():
    array_field = Array(min_items=2, max_items=2)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([1])
    assert exc_info.value.messages()[0].text == "Must have 2 items."

def test_array_validate_min_items():
    array_field = Array(min_items=2)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([1])
    assert exc_info.value.messages()[0].text == "Must have at least 2 items."

def test_array_validate_empty():
    array_field = Array(min_items=1)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([])
    assert exc_info.value.messages()[0].text == "Must not be empty."

def test_array_validate_max_items():
    array_field = Array(max_items=1)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([1, 2])
    assert exc_info.value.messages()[0].text == "Must have no more than 1 items."

def test_array_validate_unique_items():
    array_field = Array(unique_items=True)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([1, 1])
    assert exc_info.value.messages()[0].text == "Items must be unique."

def test_array_validate_items():
    item_field = DummyField()
    array_field = Array(items=item_field)
    assert array_field.validate([1, 2]) == [1, 2]

def test_array_validate_additional_items():
    item_field = DummyField()
    additional_item_field = DummyField()
    array_field = Array(items=[item_field], additional_items=additional_item_field)
    assert array_field.validate([1, 2]) == [1, 2]

def test_array_validate_error_messages():
    item_field = DummyField()
    array_field = Array(items=item_field)
    with pytest.raises(ValidationError) as exc_info:
        array_field.validate([1, "invalid"])
    assert len(exc_info.value.messages()) > 0
