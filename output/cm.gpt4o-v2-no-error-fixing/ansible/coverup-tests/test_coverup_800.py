# file: lib/ansible/parsing/splitter.py:126-138
# asked: {"lines": [135, 136, 137], "branches": [[134, 135], [136, 137], [136, 138]]}
# gained: {"lines": [135, 136, 137], "branches": [[134, 135], [136, 137], [136, 138]]}

import pytest

from ansible.parsing.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_increase_depth():
    token = "{{ open }} {{ open }}"
    cur_depth = 1
    open_token = "{{ open }}"
    close_token = "{{ close }}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 3

def test_count_jinja2_blocks_decrease_depth():
    token = "{{ close }} {{ close }}"
    cur_depth = 3
    open_token = "{{ open }}"
    close_token = "{{ close }}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 1

def test_count_jinja2_blocks_negative_depth():
    token = "{{ close }} {{ close }}"
    cur_depth = 1
    open_token = "{{ open }}"
    close_token = "{{ close }}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 0

def test_count_jinja2_blocks_equal_open_close():
    token = "{{ open }} {{ close }}"
    cur_depth = 1
    open_token = "{{ open }}"
    close_token = "{{ close }}"
    new_depth = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert new_depth == 1
