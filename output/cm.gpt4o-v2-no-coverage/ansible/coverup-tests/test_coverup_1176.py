# file: lib/ansible/parsing/splitter.py:126-138
# asked: {"lines": [135, 136, 137], "branches": [[134, 135], [136, 137], [136, 138]]}
# gained: {"lines": [135, 136, 137], "branches": [[134, 135], [136, 137], [136, 138]]}

import pytest

from ansible.parsing.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_equal_open_close():
    assert _count_jinja2_blocks("{{ test }}", 0, "{{", "}}") == 0

def test_count_jinja2_blocks_more_open():
    assert _count_jinja2_blocks("{{ test {{", 0, "{{", "}}") == 2

def test_count_jinja2_blocks_more_close():
    assert _count_jinja2_blocks("}} test }}", 2, "{{", "}}") == 0

def test_count_jinja2_blocks_negative_depth():
    assert _count_jinja2_blocks("}} test }}", 0, "{{", "}}") == 0

def test_count_jinja2_blocks_increase_depth():
    assert _count_jinja2_blocks("{{ test }} {{", 1, "{{", "}}") == 2

def test_count_jinja2_blocks_decrease_depth():
    assert _count_jinja2_blocks("{{ test }} }}", 2, "{{", "}}") == 1
