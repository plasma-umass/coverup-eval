# file: lib/ansible/modules/iptables.py:559-563
# asked: {"lines": [559, 560, 561, 562, 563], "branches": [[560, 561], [560, 562], [562, 0], [562, 563]]}
# gained: {"lines": [559, 560, 561, 562, 563], "branches": [[560, 561], [560, 562], [562, 0], [562, 563]]}

import pytest

from ansible.modules.iptables import append_match_flag

def test_append_match_flag_match():
    rule = []
    append_match_flag(rule, 'match', '--match', False)
    assert rule == ['--match']

def test_append_match_flag_negate():
    rule = []
    append_match_flag(rule, 'negate', '--match', True)
    assert rule == ['!', '--match']

def test_append_match_flag_no_negate():
    rule = []
    append_match_flag(rule, 'negate', '--match', False)
    assert rule == []

def test_append_match_flag_other_param():
    rule = []
    append_match_flag(rule, 'other', '--match', True)
    assert rule == []

