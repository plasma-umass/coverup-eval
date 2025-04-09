# file lib/ansible/utils/collection_loader/_collection_config.py:19-47
# lines [19, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 37, 39, 41, 42, 43, 44, 45, 46, 47]
# branches ['24->25', '24->26', '42->exit', '42->43', '46->42', '46->47']

import pytest

from ansible.utils.collection_loader._collection_config import _EventSource

def test_event_source_add_handler():
    event_source = _EventSource()
    
    def handler():
        pass
    
    event_source += handler
    assert handler in event_source._handlers

def test_event_source_add_non_callable_handler():
    event_source = _EventSource()
    
    with pytest.raises(ValueError, match='handler must be callable'):
        event_source += "not a callable"

def test_event_source_remove_handler():
    event_source = _EventSource()
    
    def handler():
        pass
    
    event_source += handler
    event_source -= handler
    assert handler not in event_source._handlers

def test_event_source_remove_nonexistent_handler():
    event_source = _EventSource()
    
    def handler():
        pass
    
    event_source -= handler  # Should not raise an exception

def test_event_source_fire():
    event_source = _EventSource()
    result = []
    
    def handler(arg):
        result.append(arg)
    
    event_source += handler
    event_source.fire('test')
    assert result == ['test']

def test_event_source_fire_with_exception():
    event_source = _EventSource()
    
    def handler(arg):
        raise ValueError("Test exception")
    
    event_source += handler
    
    with pytest.raises(ValueError, match="Test exception"):
        event_source.fire('test')

def test_event_source_on_exception_override():
    class CustomEventSource(_EventSource):
        def _on_exception(self, handler, exc, *args, **kwargs):
            return False  # Do not re-raise the exception
    
    event_source = CustomEventSource()
    
    def handler(arg):
        raise ValueError("Test exception")
    
    event_source += handler
    
    try:
        event_source.fire('test')
    except ValueError:
        pytest.fail("Exception should not have been raised")

