# file: lib/ansible/modules/iptables.py:566-568
# asked: {"lines": [567, 568], "branches": [[567, 0], [567, 568]]}
# gained: {"lines": [567, 568], "branches": [[567, 0], [567, 568]]}

import pytest

from ansible.modules.iptables import append_csv

def test_append_csv_with_param():
    rule = []
    param = ['value1', 'value2']
    flag = '--flag'
    append_csv(rule, param, flag)
    assert rule == ['--flag', 'value1,value2']

def test_append_csv_without_param():
    rule = []
    param = []
    flag = '--flag'
    append_csv(rule, param, flag)
    assert rule == []

def test_append_csv_with_none_param():
    rule = []
    param = None
    flag = '--flag'
    append_csv(rule, param, flag)
    assert rule == []
