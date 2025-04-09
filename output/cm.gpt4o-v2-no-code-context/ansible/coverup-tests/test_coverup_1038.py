# file: lib/ansible/modules/iptables.py:576-578
# asked: {"lines": [577, 578], "branches": [[577, 0], [577, 578]]}
# gained: {"lines": [577, 578], "branches": [[577, 0], [577, 578]]}

import pytest
from ansible.modules.iptables import append_jump

def test_append_jump_with_param():
    rule = []
    param = True
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == ['-j', 'ACCEPT']

def test_append_jump_without_param():
    rule = []
    param = False
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == []
