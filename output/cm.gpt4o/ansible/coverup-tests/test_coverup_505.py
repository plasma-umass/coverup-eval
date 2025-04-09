# file lib/ansible/modules/iptables.py:553-556
# lines [553, 554, 555, 556]
# branches ['554->exit', '554->555', '555->exit', '555->556']

import pytest
from unittest.mock import patch

# Assuming the function is part of a class or module, we need to import it correctly.
# For this example, let's assume it's a standalone function in a module named `iptables`.

from ansible.modules.iptables import append_tcp_flags

def test_append_tcp_flags():
    rule = []
    param = {
        'flags': ['SYN', 'ACK'],
        'flags_set': ['SYN']
    }
    flag = '--tcp-flags'

    append_tcp_flags(rule, param, flag)

    assert rule == ['--tcp-flags', 'SYN,ACK', 'SYN']

def test_append_tcp_flags_no_flags():
    rule = []
    param = {
        'flags': [],
        'flags_set': []
    }
    flag = '--tcp-flags'

    append_tcp_flags(rule, param, flag)

    assert rule == ['--tcp-flags', '', '']

def test_append_tcp_flags_missing_flags():
    rule = []
    param = {
        'flags_set': ['SYN']
    }
    flag = '--tcp-flags'

    append_tcp_flags(rule, param, flag)

    assert rule == []

def test_append_tcp_flags_missing_flags_set():
    rule = []
    param = {
        'flags': ['SYN', 'ACK']
    }
    flag = '--tcp-flags'

    append_tcp_flags(rule, param, flag)

    assert rule == []

def test_append_tcp_flags_no_param():
    rule = []
    param = None
    flag = '--tcp-flags'

    append_tcp_flags(rule, param, flag)

    assert rule == []
