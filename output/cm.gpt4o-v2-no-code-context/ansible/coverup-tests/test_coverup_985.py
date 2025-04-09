# file: lib/ansible/module_utils/splitter.py:53-65
# asked: {"lines": [59, 60, 61, 62, 63, 64, 65], "branches": [[61, 62], [61, 65], [63, 64], [63, 65]]}
# gained: {"lines": [59, 60, 61, 62, 63, 64, 65], "branches": [[61, 62], [61, 65], [63, 64], [63, 65]]}

import pytest

# Assuming the function _count_jinja2_blocks is accessible for testing
from ansible.module_utils.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_no_open_no_close():
    token = "some text without tokens"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0

def test_count_jinja2_blocks_equal_open_close():
    token = "{{ some text }} with equal tokens {{}}"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0

def test_count_jinja2_blocks_more_open():
    token = "{{ some text {{ with more open tokens"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 2

def test_count_jinja2_blocks_more_close():
    token = "some text }} with more close tokens }}"
    cur_depth = 2
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0

def test_count_jinja2_blocks_negative_depth():
    token = "some text }} with more close tokens }}"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0
