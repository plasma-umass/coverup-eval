# file: typesystem/fields.py:602-659
# asked: {"lines": [603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 615, 616, 617, 618, 619, 620, 621, 624, 625, 626, 627, 629, 630, 631, 632, 633, 634, 635, 636, 637, 639, 640, 642, 643, 644, 646, 648, 649, 650, 651, 652, 654, 656, 657, 659], "branches": [[603, 604], [603, 605], [605, 606], [605, 607], [607, 608], [607, 610], [610, 615], [610, 616], [616, 617], [616, 620], [617, 618], [617, 619], [620, 621], [620, 624], [626, 627], [626, 629], [629, 630], [629, 656], [631, 632], [631, 636], [632, 633], [632, 634], [634, 635], [634, 639], [636, 637], [636, 639], [639, 640], [639, 642], [643, 644], [643, 646], [648, 629], [648, 649], [649, 650], [649, 654], [656, 657], [656, 659]]}
# gained: {"lines": [603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 615, 616, 617, 618, 619, 620, 621, 624, 625, 626, 627, 629, 630, 631, 632, 633, 634, 635, 636, 637, 639, 640, 642, 643, 644, 646, 648, 649, 650, 651, 652, 654, 656, 657, 659], "branches": [[603, 604], [603, 605], [605, 606], [605, 607], [607, 608], [607, 610], [610, 615], [610, 616], [616, 617], [616, 620], [617, 618], [617, 619], [620, 621], [620, 624], [626, 627], [626, 629], [629, 630], [629, 656], [631, 632], [631, 636], [632, 633], [632, 634], [634, 635], [636, 637], [636, 639], [639, 640], [639, 642], [643, 644], [643, 646], [648, 629], [648, 649], [649, 650], [649, 654], [656, 657], [656, 659]]}

import pytest
from typesystem.fields import Array, Field, ValidationError, Message, Uniqueness

class MockField(Field):
    def validate_or_error(self, value, strict=False):
        if value == "error":
            return None, ValidationError(messages=[Message(text="error", code="error")])
        return value, None

@pytest.fixture
def array_field():
    return Array(allow_null=True, min_items=1, max_items=3, unique_items=True, items=MockField())

def test_validate_none_allowed(array_field):
    assert array_field.validate(None) is None

def test_validate_none_not_allowed():
    field = Array(allow_null=False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert excinfo.value.messages()[0].code == "null"

def test_validate_not_list():
    field = Array()
    with pytest.raises(ValidationError) as excinfo:
        field.validate("not a list")
    assert excinfo.value.messages()[0].code == "type"

def test_validate_exact_items():
    field = Array(min_items=2, max_items=2)
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1])
    assert excinfo.value.messages()[0].code == "exact_items"

def test_validate_min_items():
    field = Array(min_items=2)
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1])
    assert excinfo.value.messages()[0].code == "min_items"

def test_validate_max_items():
    field = Array(max_items=2)
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1, 2, 3])
    assert excinfo.value.messages()[0].code == "max_items"

def test_validate_empty():
    field = Array(min_items=1)
    with pytest.raises(ValidationError) as excinfo:
        field.validate([])
    assert excinfo.value.messages()[0].code == "empty"

def test_validate_unique_items():
    field = Array(unique_items=True)
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1, 1])
    assert excinfo.value.messages()[0].code == "unique_items"

def test_validate_items():
    field = Array(items=MockField())
    assert field.validate([1, 2, 3]) == [1, 2, 3]

def test_validate_items_with_error():
    field = Array(items=MockField())
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1, "error", 3])
    assert excinfo.value.messages()[0].code == "error"

def test_validate_additional_items():
    field = Array(items=[MockField()], additional_items=MockField())
    assert field.validate([1, 2]) == [1, 2]

def test_validate_additional_items_with_error():
    field = Array(items=[MockField()], additional_items=MockField())
    with pytest.raises(ValidationError) as excinfo:
        field.validate([1, "error"])
    assert excinfo.value.messages()[0].code == "error"
