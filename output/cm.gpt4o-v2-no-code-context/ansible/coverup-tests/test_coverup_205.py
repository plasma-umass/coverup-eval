# file: lib/ansible/modules/iptables.py:541-550
# asked: {"lines": [541, 542, 543, 544, 546, 547, 548, 550], "branches": [[542, 543], [542, 546], [543, 0], [543, 544], [546, 0], [546, 547], [547, 548], [547, 550]]}
# gained: {"lines": [541, 542, 543, 544, 546, 547, 548, 550], "branches": [[542, 543], [542, 546], [543, 0], [543, 544], [546, 0], [546, 547], [547, 548], [547, 550]]}

import pytest

# Assuming the append_param function is imported from the module
from ansible.modules.iptables import append_param

def test_append_param_with_list(monkeypatch):
    rule = []
    param = ['param1', 'param2']
    flag = '--flag'
    is_list = True

    append_param(rule, param, flag, is_list)

    assert rule == ['--flag', 'param1', '--flag', 'param2']

def test_append_param_with_not_none_param(monkeypatch):
    rule = []
    param = 'param'
    flag = '--flag'
    is_list = False

    append_param(rule, param, flag, is_list)

    assert rule == ['--flag', 'param']

def test_append_param_with_exclamation(monkeypatch):
    rule = []
    param = '!param'
    flag = '--flag'
    is_list = False

    append_param(rule, param, flag, is_list)

    assert rule == ['!', '--flag', 'param']

def test_append_param_with_none_param(monkeypatch):
    rule = []
    param = None
    flag = '--flag'
    is_list = False

    append_param(rule, param, flag, is_list)

    assert rule == []
