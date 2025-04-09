# file: flutes/structure.py:60-71
# asked: {"lines": [60, 61, 67, 68, 69, 70, 71], "branches": []}
# gained: {"lines": [60, 61, 67, 68, 69, 70, 71], "branches": []}

import pytest
from flutes.structure import no_map_instance, _NO_MAP_INSTANCE_ATTR

class TestNoMapInstance:
    def test_no_map_instance_sets_attribute(self):
        class TestClass:
            pass

        instance = TestClass()
        no_map_instance(instance)
        assert getattr(instance, _NO_MAP_INSTANCE_ATTR, False) is True

    def test_no_map_instance_handles_attribute_error(self, monkeypatch):
        class TestClass:
            def __setattr__(self, name, value):
                raise AttributeError("Cannot set attribute")

        instance = TestClass()

        class MockNoMapType:
            def __init__(self, instance):
                self.instance = instance

        monkeypatch.setattr('flutes.structure._no_map_type', lambda x: MockNoMapType)
        result = no_map_instance(instance)
        assert isinstance(result, MockNoMapType)
        assert result.instance is instance
