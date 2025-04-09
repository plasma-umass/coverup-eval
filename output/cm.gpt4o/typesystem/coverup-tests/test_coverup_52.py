# file typesystem/fields.py:562-600
# lines [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600]
# branches ['586->587', '586->592', '587->588', '587->589', '589->590', '589->592', '592->593', '592->596']

import pytest
import typing
from typesystem.fields import Field

class Array(Field):
    def __init__(
        self,
        items: typing.Union[Field, typing.Sequence[Field]] = None,
        additional_items: typing.Union[Field, bool] = False,
        min_items: int = None,
        max_items: int = None,
        exact_items: int = None,
        unique_items: bool = False,
        **kwargs: typing.Any,
    ) -> None:
        super().__init__(**kwargs)

        items = list(items) if isinstance(items, (list, tuple)) else items

        assert (
            items is None
            or isinstance(items, Field)
            or (isinstance(items, list) and all(isinstance(i, Field) for i in items))
        )
        assert isinstance(additional_items, bool) or isinstance(additional_items, Field)
        assert min_items is None or isinstance(min_items, int)
        assert max_items is None or isinstance(max_items, int)
        assert isinstance(unique_items, bool)

        if isinstance(items, list):
            if min_items is None:
                min_items = len(items)
            if max_items is None and (additional_items is False):
                max_items = len(items)

        if exact_items is not None:
            min_items = exact_items
            max_items = exact_items

        self.items = items
        self.additional_items = additional_items
        self.min_items = min_items
        self.max_items = max_items
        self.unique_items = unique_items

class TestArrayField:
    def test_array_field_initialization(self):
        # Mock Field class for testing
        class MockField(Field):
            pass

        # Test with items as a single Field instance
        field_instance = MockField()
        array_field = Array(items=field_instance)
        assert array_field.items == field_instance
        assert array_field.min_items is None
        assert array_field.max_items is None
        assert array_field.unique_items is False

        # Test with items as a list of Field instances
        field_instance_list = [MockField(), MockField()]
        array_field = Array(items=field_instance_list)
        assert array_field.items == field_instance_list
        assert array_field.min_items == len(field_instance_list)
        assert array_field.max_items == len(field_instance_list)
        assert array_field.unique_items is False

        # Test with additional_items as a Field instance
        additional_field = MockField()
        array_field = Array(items=field_instance_list, additional_items=additional_field)
        assert array_field.additional_items == additional_field

        # Test with min_items, max_items, and unique_items
        array_field = Array(items=field_instance_list, min_items=1, max_items=3, unique_items=True)
        assert array_field.min_items == 1
        assert array_field.max_items == 3
        assert array_field.unique_items is True

        # Test with exact_items
        array_field = Array(items=field_instance_list, exact_items=2)
        assert array_field.min_items == 2
        assert array_field.max_items == 2

        # Test with items as None
        array_field = Array()
        assert array_field.items is None
        assert array_field.min_items is None
        assert array_field.max_items is None
        assert array_field.unique_items is False

    def test_array_field_assertions(self):
        class MockField(Field):
            pass

        # Test invalid items type
        with pytest.raises(AssertionError):
            Array(items="invalid")

        # Test invalid additional_items type
        with pytest.raises(AssertionError):
            Array(additional_items="invalid")

        # Test invalid min_items type
        with pytest.raises(AssertionError):
            Array(min_items="invalid")

        # Test invalid max_items type
        with pytest.raises(AssertionError):
            Array(max_items="invalid")

        # Test invalid unique_items type
        with pytest.raises(AssertionError):
            Array(unique_items="invalid")
