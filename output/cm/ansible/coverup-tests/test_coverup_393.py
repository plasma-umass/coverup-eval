# file lib/ansible/module_utils/splitter.py:53-65
# lines [53, 59, 60, 61, 62, 63, 64, 65]
# branches ['61->62', '61->65', '63->64', '63->65']

import pytest
from ansible.module_utils.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_uneven_open_close():
    token = "{{ some_var }}"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    # This should not change cur_depth because the number of open and close tokens is the same
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0

    token = "{{ some_var"
    cur_depth = 0
    # This should increase cur_depth by 1
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 1

    token = "}}"
    cur_depth = new_depth
    # This should decrease cur_depth back to 0
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0

    token = "}}"
    cur_depth = -1  # Simulate an incorrect cur_depth
    # This should correct cur_depth back to 0
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0
