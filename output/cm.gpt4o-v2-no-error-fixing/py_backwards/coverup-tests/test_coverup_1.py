# file: py_backwards/transformers/six_moves.py:21-26
# asked: {"lines": [21, 22, 23, 24, 25, 26], "branches": [[24, 25], [24, 26]]}
# gained: {"lines": [21, 22, 23, 24, 25, 26], "branches": [[24, 25], [24, 26]]}

import pytest
from py_backwards.transformers.six_moves import MovedModule

def test_moved_module_with_new_none():
    module = MovedModule(name="module_name", old="old_module")
    assert module.name == "module_name"
    assert module.new == "module_name"

def test_moved_module_with_new_provided():
    module = MovedModule(name="module_name", old="old_module", new="new_module")
    assert module.name == "module_name"
    assert module.new == "new_module"
