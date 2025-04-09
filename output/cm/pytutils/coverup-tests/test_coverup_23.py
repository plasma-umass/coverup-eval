# file pytutils/lazy/lazy_import.py:115-118
# lines [115, 116, 117, 118]
# branches ['116->117', '116->118']

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_equality():
    # Create two instances of IllegalUseOfScopeReplacer with required arguments
    exception1 = IllegalUseOfScopeReplacer('name', 'msg')
    exception2 = IllegalUseOfScopeReplacer('name', 'msg')

    # Test equality of the same class and dict
    assert exception1 == exception2

    # Test equality with different class
    assert not (exception1 == Exception())

    # Test equality with NotImplemented case
    class DifferentClass:
        pass

    different_instance = DifferentClass()
    assert (exception1 == different_instance) is NotImplemented or (exception1 != different_instance)
