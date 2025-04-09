# file: lib/ansible/utils/collection_loader/_collection_config.py:19-47
# asked: {"lines": [19, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 37, 39, 41, 42, 43, 44, 45, 46, 47], "branches": [[24, 25], [24, 26], [42, 0], [42, 43], [46, 42], [46, 47]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 37, 39, 41, 42, 43, 44, 45, 46, 47], "branches": [[24, 25], [24, 26], [42, 0], [42, 43], [46, 47]]}

import pytest

from ansible.utils.collection_loader._collection_config import _EventSource

def test_eventsource_iadd_callable():
    event_source = _EventSource()
    handler = lambda x: x
    event_source += handler
    assert handler in event_source._handlers

def test_eventsource_iadd_not_callable():
    event_source = _EventSource()
    with pytest.raises(ValueError, match="handler must be callable"):
        event_source += "not a callable"

def test_eventsource_isub_existing_handler():
    event_source = _EventSource()
    handler = lambda x: x
    event_source += handler
    event_source -= handler
    assert handler not in event_source._handlers

def test_eventsource_isub_non_existing_handler():
    event_source = _EventSource()
    handler = lambda x: x
    event_source -= handler  # Should not raise an exception

def test_eventsource_fire_with_handler():
    event_source = _EventSource()
    result = []

    def handler(x):
        result.append(x)

    event_source += handler
    event_source.fire(42)
    assert result == [42]

def test_eventsource_fire_with_exception():
    event_source = _EventSource()

    def handler(x):
        raise ValueError("Test exception")

    event_source += handler
    with pytest.raises(ValueError, match="Test exception"):
        event_source.fire(42)
