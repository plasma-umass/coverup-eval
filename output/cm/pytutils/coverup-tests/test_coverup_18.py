# file pytutils/lazy/lazy_import.py:52-60
# lines [52, 53, 54, 55, 56, 58, 60]
# branches ['55->56', '55->58']

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_with_extra():
    name = "test_name"
    msg = "test message"
    extra = "additional information"
    
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer(name, msg, extra)
    
    exception = exc_info.value
    assert exception.name == name
    assert exception.msg == msg
    assert exception.extra == ': ' + str(extra)

def test_illegal_use_of_scope_replacer_without_extra():
    name = "test_name"
    msg = "test message"
    
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer(name, msg)
    
    exception = exc_info.value
    assert exception.name == name
    assert exception.msg == msg
    assert exception.extra == ''
