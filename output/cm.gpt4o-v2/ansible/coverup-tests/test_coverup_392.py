# file: lib/ansible/parsing/splitter.py:126-138
# asked: {"lines": [126, 132, 133, 134, 135, 136, 137, 138], "branches": [[134, 135], [134, 138], [136, 137], [136, 138]]}
# gained: {"lines": [126, 132, 133, 134, 135, 136, 137, 138], "branches": [[134, 135], [134, 138], [136, 137], [136, 138]]}

import pytest
from ansible.parsing.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_increase_depth():
    token = "{{ test {{"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 2

def test_count_jinja2_blocks_decrease_depth():
    token = "}} test }}"
    cur_depth = 2
    open_token = "{{"
    close_token = "}}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0

def test_count_jinja2_blocks_no_change():
    token = "{{ test }}"
    cur_depth = 1
    open_token = "{{"
    close_token = "}}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 1

def test_count_jinja2_blocks_negative_depth():
    token = "}} test }}"
    cur_depth = 1
    open_token = "{{"
    close_token = "}}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0
