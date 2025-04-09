# file lib/ansible/parsing/splitter.py:126-138
# lines [126, 132, 133, 134, 135, 136, 137, 138]
# branches ['134->135', '134->138', '136->137', '136->138']

import pytest

# Assuming the function _count_jinja2_blocks is in the module ansible.parsing.splitter
from ansible.parsing.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_uneven_open_close():
    # Test with more open tokens than close tokens
    token = "{{ some_var"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 1

    # Test with more close tokens than open tokens
    token = "some_var }}"
    cur_depth = 1
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0

    # Test with equal number of open and close tokens
    token = "{{ some_var }}"
    cur_depth = 0
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == cur_depth

    # Test with negative depth adjustment resulting in negative depth (should reset to 0)
    token = "}}"
    cur_depth = 0
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0
