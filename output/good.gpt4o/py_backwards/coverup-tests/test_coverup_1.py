# file py_backwards/transformers/six_moves.py:21-26
# lines [21, 22, 23, 24, 25, 26]
# branches ['24->25', '24->26']

import pytest
from py_backwards.transformers.six_moves import MovedModule

def test_moved_module_initialization():
    # Test case where new is provided
    module_with_new = MovedModule(name="old_module", old="old_path", new="new_path")
    assert module_with_new.name == "old_module"
    assert module_with_new.new == "new_path"

    # Test case where new is None
    module_without_new = MovedModule(name="old_module", old="old_path")
    assert module_without_new.name == "old_module"
    assert module_without_new.new == "old_module"
