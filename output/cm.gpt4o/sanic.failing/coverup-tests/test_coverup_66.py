# file sanic/blueprint_group.py:116-128
# lines [116, 128]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    @pytest.fixture
    def blueprint_group(self):
        class MockBlueprint:
            pass

        class TestBlueprintGroup(BlueprintGroup):
            def __init__(self):
                self._blueprints = [MockBlueprint() for _ in range(5)]

            def __len__(self):
                return len(self._blueprints)

            def __setitem__(self, index, value):
                self._blueprints[index] = value

            def __delitem__(self, index):
                del self._blueprints[index]

            def insert(self, index, value):
                self._blueprints.insert(index, value)

        return TestBlueprintGroup()

    def test_getitem(self, blueprint_group):
        blueprint = blueprint_group[2]
        assert isinstance(blueprint, object)

    def test_getitem_out_of_range(self, blueprint_group):
        with pytest.raises(IndexError):
            _ = blueprint_group[10]
