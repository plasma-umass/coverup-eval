# file: lib/ansible/modules/iptables.py:553-556
# asked: {"lines": [554, 555, 556], "branches": [[554, 0], [554, 555], [555, 0], [555, 556]]}
# gained: {"lines": [554, 555, 556], "branches": [[554, 0], [554, 555], [555, 0], [555, 556]]}

import pytest

from ansible.modules.iptables import append_tcp_flags

def test_append_tcp_flags_with_flags_and_flags_set():
    rule = []
    param = {'flags': ['SYN', 'ACK'], 'flags_set': ['SYN']}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == ['--tcp-flags', 'SYN,ACK', 'SYN']

def test_append_tcp_flags_without_flags():
    rule = []
    param = {'flags_set': ['SYN']}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == []

def test_append_tcp_flags_without_flags_set():
    rule = []
    param = {'flags': ['SYN', 'ACK']}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == []

def test_append_tcp_flags_with_empty_param():
    rule = []
    param = {}
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == []

def test_append_tcp_flags_with_none_param():
    rule = []
    param = None
    append_tcp_flags(rule, param, '--tcp-flags')
    assert rule == []
