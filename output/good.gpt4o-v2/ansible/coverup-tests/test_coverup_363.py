# file: lib/ansible/module_utils/splitter.py:53-65
# asked: {"lines": [53, 59, 60, 61, 62, 63, 64, 65], "branches": [[61, 62], [61, 65], [63, 64], [63, 65]]}
# gained: {"lines": [53, 59, 60, 61, 62, 63, 64, 65], "branches": [[61, 62], [61, 65], [63, 64], [63, 65]]}

import pytest

from ansible.module_utils.splitter import _count_jinja2_blocks

def test_count_jinja2_blocks_equal_tokens():
    assert _count_jinja2_blocks("{{ test }}", 0, "{{", "}}") == 0

def test_count_jinja2_blocks_more_open_tokens():
    assert _count_jinja2_blocks("{{ test {{", 0, "{{", "}}") == 2

def test_count_jinja2_blocks_more_close_tokens():
    assert _count_jinja2_blocks("}} test }}", 0, "{{", "}}") == 0

def test_count_jinja2_blocks_depth_increase():
    assert _count_jinja2_blocks("{{ test {{", 2, "{{", "}}") == 4

def test_count_jinja2_blocks_depth_decrease():
    assert _count_jinja2_blocks("}} test }}", 2, "{{", "}}") == 0

def test_count_jinja2_blocks_depth_negative():
    assert _count_jinja2_blocks("}} test }}", 0, "{{", "}}") == 0
