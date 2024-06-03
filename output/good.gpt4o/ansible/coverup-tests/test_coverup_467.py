# file lib/ansible/modules/iptables.py:559-563
# lines [559, 560, 561, 562, 563]
# branches ['560->561', '560->562', '562->exit', '562->563']

import pytest
from ansible.modules.iptables import append_match_flag

def test_append_match_flag():
    # Test case where param is 'match'
    rule = []
    append_match_flag(rule, 'match', '--match', False)
    assert rule == ['--match']

    # Test case where param is 'negate' and negatable is True
    rule = []
    append_match_flag(rule, 'negate', '--match', True)
    assert rule == ['!', '--match']

    # Test case where param is 'negate' and negatable is False
    rule = []
    append_match_flag(rule, 'negate', '--match', False)
    assert rule == []

    # Test case where param is neither 'match' nor 'negate'
    rule = []
    append_match_flag(rule, 'other', '--match', True)
    assert rule == []

    # Test case where param is 'match' and negatable is True
    rule = []
    append_match_flag(rule, 'match', '--match', True)
    assert rule == ['--match']

    # Test case where param is 'negate' and negatable is True with existing rule
    rule = ['-A', 'INPUT']
    append_match_flag(rule, 'negate', '--match', True)
    assert rule == ['-A', 'INPUT', '!', '--match']

    # Test case where param is 'match' with existing rule
    rule = ['-A', 'INPUT']
    append_match_flag(rule, 'match', '--match', False)
    assert rule == ['-A', 'INPUT', '--match']
