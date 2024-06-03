# file httpie/utils.py:22-65
# lines [22, 48, 57, 58, 60, 61, 62, 65]
# branches ['57->58', '57->60', '60->61', '60->65', '61->60', '61->62']

import pytest
from httpie.utils import humanize_bytes

def test_humanize_bytes():
    # Test cases from the docstring
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'

    # Additional test cases to ensure full coverage
    assert humanize_bytes(0) == '0.00 B'
    assert humanize_bytes(1023) == '1023.00 B'
    assert humanize_bytes(1024 * 1024 * 1024 * 1024 * 1024, precision=2) == '1.00 PB'
    assert humanize_bytes(1024 * 1024 * 1024 * 1024, precision=2) == '1.00 TB'
    assert humanize_bytes(1024 * 1024 * 1024, precision=2) == '1.00 GB'
    assert humanize_bytes(1024 * 1024, precision=2) == '1.00 MB'
    assert humanize_bytes(1024, precision=2) == '1.00 kB'
