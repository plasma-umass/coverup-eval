# file: lib/ansible/modules/iptables.py:553-556
# asked: {"lines": [553, 554, 555, 556], "branches": [[554, 0], [554, 555], [555, 0], [555, 556]]}
# gained: {"lines": [553, 554, 555, 556], "branches": [[554, 0], [554, 555], [555, 0], [555, 556]]}

import pytest

# Assuming the append_tcp_flags function is part of a module named iptables
from ansible.modules.iptables import append_tcp_flags

def test_append_tcp_flags_with_flags_and_flags_set():
    rule = []
    param = {
        'flags': ['SYN', 'ACK'],
        'flags_set': ['SYN']
    }
    flag = '--tcp-flags'
    
    append_tcp_flags(rule, param, flag)
    
    assert rule == ['--tcp-flags', 'SYN,ACK', 'SYN']

def test_append_tcp_flags_with_empty_param():
    rule = []
    param = {}
    flag = '--tcp-flags'
    
    append_tcp_flags(rule, param, flag)
    
    assert rule == []

def test_append_tcp_flags_with_flags_only():
    rule = []
    param = {
        'flags': ['SYN', 'ACK']
    }
    flag = '--tcp-flags'
    
    append_tcp_flags(rule, param, flag)
    
    assert rule == []

def test_append_tcp_flags_with_flags_set_only():
    rule = []
    param = {
        'flags_set': ['SYN']
    }
    flag = '--tcp-flags'
    
    append_tcp_flags(rule, param, flag)
    
    assert rule == []
