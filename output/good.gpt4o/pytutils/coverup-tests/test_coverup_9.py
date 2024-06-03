# file pytutils/lazy/lazy_import.py:52-60
# lines [52, 53, 54, 55, 56, 58, 60]
# branches ['55->56', '55->58']

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer():
    # Test with extra parameter
    exception_with_extra = IllegalUseOfScopeReplacer("TestName", "Test message", extra="Extra info")
    assert exception_with_extra.name == "TestName"
    assert exception_with_extra.msg == "Test message"
    assert exception_with_extra.extra == ": Extra info"
    
    # Test without extra parameter
    exception_without_extra = IllegalUseOfScopeReplacer("TestName", "Test message")
    assert exception_without_extra.name == "TestName"
    assert exception_without_extra.msg == "Test message"
    assert exception_without_extra.extra == ""
    
    # Ensure the exception is properly raised
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer("TestName", "Test message", extra="Extra info")
    assert exc_info.value.name == "TestName"
    assert exc_info.value.msg == "Test message"
    assert exc_info.value.extra == ": Extra info"
