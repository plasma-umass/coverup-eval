# file lib/ansible/modules/iptables.py:576-578
# lines [576, 577, 578]
# branches ['577->exit', '577->578']

import pytest
from ansible.modules.iptables import append_jump

def test_append_jump_with_param():
    rule = ['-A', 'INPUT']
    param = True
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == ['-A', 'INPUT', '-j', 'ACCEPT']

def test_append_jump_without_param():
    rule = ['-A', 'INPUT']
    param = False
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == ['-A', 'INPUT']
