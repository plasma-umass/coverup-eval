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
        assert blueprint is not None
        assert isinstance(blueprint, object)

    def test_getitem_slice(self, blueprint_group):
        blueprints = blueprint_group[1:3]
        assert len(blueprints) == 2
        assert all(isinstance(bp, object) for bp in blueprints)
