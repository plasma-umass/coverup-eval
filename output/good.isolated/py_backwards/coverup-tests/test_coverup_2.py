# file py_backwards/transformers/six_moves.py:21-26
# lines [21, 22, 23, 24, 25, 26]
# branches ['24->25', '24->26']

import pytest
from py_backwards.transformers.six_moves import MovedModule

def test_moved_module_init():
    # Test with new parameter provided
    moved_module_with_new = MovedModule(name='module_name', old='old_module', new='new_module')
    assert moved_module_with_new.name == 'module_name'
    assert moved_module_with_new.new == 'new_module'

    # Test without new parameter provided (should default to name)
    moved_module_without_new = MovedModule(name='module_name', old='old_module')
    assert moved_module_without_new.name == 'module_name'
    assert moved_module_without_new.new == 'module_name'
