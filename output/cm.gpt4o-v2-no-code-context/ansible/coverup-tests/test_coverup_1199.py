# file: lib/ansible/utils/collection_loader/_collection_config.py:19-47
# asked: {"lines": [], "branches": [[46, 42]]}
# gained: {"lines": [], "branches": [[46, 42]]}

import pytest

from ansible.utils.collection_loader._collection_config import _EventSource

def test_event_source_add_handler():
    event_source = _EventSource()
    handler = lambda x: x
    event_source += handler
    assert handler in event_source._handlers

def test_event_source_add_non_callable_handler():
    event_source = _EventSource()
    with pytest.raises(ValueError, match='handler must be callable'):
        event_source += "not a callable"

def test_event_source_remove_handler():
    event_source = _EventSource()
    handler = lambda x: x
    event_source += handler
    event_source -= handler
    assert handler not in event_source._handlers

def test_event_source_remove_nonexistent_handler():
    event_source = _EventSource()
    handler = lambda x: x
    event_source -= handler  # Should not raise an exception

def test_event_source_fire_with_exception(monkeypatch):
    event_source = _EventSource()
    
    def handler(x):
        raise ValueError("Test exception")
    
    event_source += handler
    
    def mock_on_exception(handler, exc, *args, **kwargs):
        return True
    
    monkeypatch.setattr(event_source, '_on_exception', mock_on_exception)
    
    with pytest.raises(ValueError, match="Test exception"):
        event_source.fire(42)

def test_event_source_fire_without_exception(monkeypatch):
    event_source = _EventSource()
    
    def handler(x):
        raise ValueError("Test exception")
    
    event_source += handler
    
    def mock_on_exception(handler, exc, *args, **kwargs):
        return False
    
    monkeypatch.setattr(event_source, '_on_exception', mock_on_exception)
    
    event_source.fire(42)  # Should not raise an exception

def test_event_source_fire_no_handlers():
    event_source = _EventSource()
    event_source.fire(42)  # Should not raise an exception
