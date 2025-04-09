# file pytutils/lazy/lazy_import.py:115-118
# lines [115, 116, 117, 118]
# branches ['116->117', '116->118']

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_equality():
    # Create two instances of the exception with the same state
    exc1 = IllegalUseOfScopeReplacer('name1', 'msg1')
    exc2 = IllegalUseOfScopeReplacer('name1', 'msg1')
    
    # Verify that they are considered equal
    assert exc1 == exc2
    
    # Create another instance with a different state
    exc3 = IllegalUseOfScopeReplacer('name2', 'msg2')
    
    # Verify that they are not considered equal
    assert exc1 != exc3

    # Verify that comparison with a different class returns NotImplemented
    assert exc1.__eq__(object()) is NotImplemented
