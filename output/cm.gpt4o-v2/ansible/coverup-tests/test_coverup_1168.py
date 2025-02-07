# file: lib/ansible/utils/collection_loader/_collection_config.py:19-47
# asked: {"lines": [25, 30, 31, 32, 33, 35, 39, 45, 46, 47], "branches": [[24, 25], [46, 42], [46, 47]]}
# gained: {"lines": [25, 30, 31, 32, 33, 35, 39, 45, 46, 47], "branches": [[24, 25], [46, 47]]}

import pytest

from ansible.utils.collection_loader._collection_config import _EventSource

def test_eventsource_iadd_non_callable():
    event_source = _EventSource()
    with pytest.raises(ValueError, match="handler must be callable"):
        event_source += "not a callable"

def test_eventsource_isub_keyerror():
    event_source = _EventSource()
    handler = lambda x: x
    event_source += handler
    event_source -= handler
    # Removing again to trigger KeyError and pass
    event_source -= handler
    assert handler not in event_source._handlers

def test_eventsource_on_exception():
    event_source = _EventSource()
    handler = lambda x: x
    exc = Exception("test exception")
    assert event_source._on_exception(handler, exc) is True

def test_eventsource_fire_with_exception():
    event_source = _EventSource()
    
    def handler(*args, **kwargs):
        raise Exception("handler exception")
    
    event_source += handler
    
    with pytest.raises(Exception, match="handler exception"):
        event_source.fire()

def test_eventsource_fire_without_exception():
    event_source = _EventSource()
    result = []

    def handler(*args, **kwargs):
        result.append("handler called")
    
    event_source += handler
    event_source.fire()
    
    assert "handler called" in result
