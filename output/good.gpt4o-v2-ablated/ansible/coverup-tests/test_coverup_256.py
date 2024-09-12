# file: lib/ansible/modules/iptables.py:571-573
# asked: {"lines": [571, 572, 573], "branches": [[572, 0], [572, 573]]}
# gained: {"lines": [571, 572, 573], "branches": [[572, 0], [572, 573]]}

import pytest

from ansible.modules.iptables import append_match

def test_append_match_with_param():
    rule = []
    param = True
    match = 'tcp'
    append_match(rule, param, match)
    assert rule == ['-m', 'tcp']

def test_append_match_without_param():
    rule = []
    param = False
    match = 'tcp'
    append_match(rule, param, match)
    assert rule == []

def test_append_match_with_different_match():
    rule = []
    param = True
    match = 'udp'
    append_match(rule, param, match)
    assert rule == ['-m', 'udp']
