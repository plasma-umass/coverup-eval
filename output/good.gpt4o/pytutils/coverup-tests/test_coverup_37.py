# file pytutils/lazy/lazy_import.py:105-106
# lines [106]
# branches []

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_repr():
    class CustomIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg

    exception_instance = CustomIllegalUseOfScopeReplacer("Test message")
    repr_output = repr(exception_instance)
    assert repr_output == "CustomIllegalUseOfScopeReplacer(Test message)"
