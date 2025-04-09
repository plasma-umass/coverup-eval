# file: lib/ansible/modules/iptables.py:581-583
# asked: {"lines": [581, 582, 583], "branches": [[582, 0], [582, 583]]}
# gained: {"lines": [581, 582, 583], "branches": [[582, 0], [582, 583]]}

import pytest

# Assuming the append_wait function is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named iptables.

from ansible.modules.iptables import append_wait

def test_append_wait_with_param():
    rule = []
    param = 'some_param'
    flag = '--wait'
    append_wait(rule, param, flag)
    assert rule == ['--wait', 'some_param']

def test_append_wait_without_param():
    rule = []
    param = None
    flag = '--wait'
    append_wait(rule, param, flag)
    assert rule == []

# Clean up is not necessary in this case as the function does not modify any global state.
