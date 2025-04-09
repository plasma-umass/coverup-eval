# file: lib/ansible/vars/manager.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

def test_extra_vars_property():
    vm = VariableManager()
    assert vm.extra_vars == vm._extra_vars
