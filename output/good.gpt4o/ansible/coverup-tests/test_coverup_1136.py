# file lib/ansible/module_utils/splitter.py:53-65
# lines [59, 60, 61, 62, 63, 64, 65]
# branches ['61->62', '61->65', '63->64', '63->65']

import pytest
from ansible.module_utils.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks():
    # Test case where num_open != num_close and cur_depth is adjusted
    token = "{{ open }} close }}"
    cur_depth = 1
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0  # cur_depth should be adjusted to 0

    # Test case where num_open != num_close and cur_depth goes negative
    token = "{{ open }} close }}"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0  # cur_depth should be adjusted to 0

    # Test case where num_open == num_close
    token = "{{ open }} {{ close }}"
    cur_depth = 1
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 1  # cur_depth should remain unchanged

    # Test case where num_open > num_close
    token = "{{ open {{ close }}"
    cur_depth = 1
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 2  # cur_depth should be increased by 1

    # Test case where num_open < num_close
    token = "{{ open }} close }}"
    cur_depth = 2
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 1  # cur_depth should be decreased by 1
