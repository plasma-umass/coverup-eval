# file lib/ansible/modules/iptables.py:559-563
# lines [559, 560, 561, 562, 563]
# branches ['560->561', '560->562', '562->exit', '562->563']

import pytest

# Assuming the function append_match_flag is in the iptables module
from ansible.modules.iptables import append_match_flag

def test_append_match_flag():
    # Test data
    rule = []
    param = 'match'
    flag = '--flag'
    negatable = True

    # Call the function with 'match'
    append_match_flag(rule, param, flag, negatable)
    assert rule == ['--flag'], "The flag should be appended when param is 'match'"

    # Reset rule list
    rule = []

    # Call the function with 'negate'
    param = 'negate'
    append_match_flag(rule, param, flag, negatable)
    assert rule == ['!', '--flag'], "The flag should be negated and appended when param is 'negate'"

    # Reset rule list
    rule = []

    # Call the function with non-negatable
    negatable = False
    append_match_flag(rule, param, flag, negatable)
    assert rule == [], "The rule should remain unchanged when negatable is False"
