# file httpie/utils.py:22-65
# lines [22, 48, 57, 58, 60, 61, 62, 65]
# branches ['57->58', '57->60', '60->61', '60->65', '61->60', '61->62']

import pytest
from httpie.utils import humanize_bytes

def test_humanize_bytes():
    assert humanize_bytes(0) == '0.00 B'
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(500) == '500.00 B'
    assert humanize_bytes(1023) == '1023.00 B'
    assert humanize_bytes(1024) == '1.00 kB'
    assert humanize_bytes(1024 * 1024) == '1.00 MB'
    assert humanize_bytes(1024 * 1024 * 1024) == '1.00 GB'
    assert humanize_bytes(1024 * 1024 * 1024 * 1024) == '1.00 TB'
    assert humanize_bytes(1024 * 1024 * 1024 * 1024 * 1024) == '1.00 PB'
    assert humanize_bytes(1024 * 1024 * 1024 * 1024 * 1024 * 1024) == '1024.00 PB'
