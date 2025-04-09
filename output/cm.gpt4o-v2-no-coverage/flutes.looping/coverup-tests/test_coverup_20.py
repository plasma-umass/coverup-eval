# file: flutes/structure.py:39-46
# asked: {"lines": [39, 46], "branches": []}
# gained: {"lines": [39, 46], "branches": []}

import pytest
from flutes.structure import register_no_map_class

def test_register_no_map_class(monkeypatch):
    class DummyContainer:
        pass

    # Create a mock _NO_MAP_TYPES set
    mock_no_map_types = set()
    monkeypatch.setattr('flutes.structure._NO_MAP_TYPES', mock_no_map_types)

    # Ensure DummyContainer is not in _NO_MAP_TYPES before the test
    assert DummyContainer not in mock_no_map_types

    # Register DummyContainer
    register_no_map_class(DummyContainer)

    # Verify that DummyContainer is now in _NO_MAP_TYPES
    assert DummyContainer in mock_no_map_types

    # Clean up by removing DummyContainer from _NO_MAP_TYPES
    mock_no_map_types.remove(DummyContainer)
    assert DummyContainer not in mock_no_map_types
