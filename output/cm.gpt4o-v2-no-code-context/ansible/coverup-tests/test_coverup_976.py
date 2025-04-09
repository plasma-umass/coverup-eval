# file: lib/ansible/utils/collection_loader/_collection_config.py:19-47
# asked: {"lines": [25, 30, 31, 32, 33, 35, 39, 45, 46, 47], "branches": [[24, 25], [46, 42], [46, 47]]}
# gained: {"lines": [25, 30, 31, 32, 33, 35, 39, 45, 46, 47], "branches": [[24, 25], [46, 47]]}

import pytest

from ansible.utils.collection_loader._collection_config import _EventSource

def test_iadd_non_callable():
    event_source = _EventSource()
    with pytest.raises(ValueError, match='handler must be callable'):
        event_source += "not a callable"

def test_isub_non_existent_handler():
    event_source = _EventSource()
    def handler():
        pass
    event_source += handler
    event_source -= handler
    # Removing again should not raise an error
    event_source -= handler

def test_fire_with_exception():
    event_source = _EventSource()
    
    def handler(*args, **kwargs):
        raise RuntimeError("Test exception")
    
    event_source += handler
    
    with pytest.raises(RuntimeError, match="Test exception"):
        event_source.fire()

def test_fire_without_exception():
    event_source = _EventSource()
    result = []

    def handler(*args, **kwargs):
        result.append("handler called")
    
    event_source += handler
    event_source.fire()
    
    assert result == ["handler called"]

def test_on_exception():
    event_source = _EventSource()
    
    def handler(*args, **kwargs):
        raise RuntimeError("Test exception")
    
    event_source += handler
    
    with pytest.raises(RuntimeError, match="Test exception"):
        event_source.fire()
