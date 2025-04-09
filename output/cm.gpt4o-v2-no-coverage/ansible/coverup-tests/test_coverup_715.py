# file: lib/ansible/modules/iptables.py:581-583
# asked: {"lines": [581, 582, 583], "branches": [[582, 0], [582, 583]]}
# gained: {"lines": [581, 582, 583], "branches": [[582, 0], [582, 583]]}

import pytest

from ansible.modules.iptables import append_wait

def test_append_wait_with_param():
    rule = []
    param = 'param_value'
    flag = 'flag_value'
    append_wait(rule, param, flag)
    assert rule == ['flag_value', 'param_value']

def test_append_wait_without_param():
    rule = []
    param = None
    flag = 'flag_value'
    append_wait(rule, param, flag)
    assert rule == []
