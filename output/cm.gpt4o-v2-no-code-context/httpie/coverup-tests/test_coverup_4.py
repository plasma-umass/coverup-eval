# file: httpie/utils.py:22-65
# asked: {"lines": [22, 48, 57, 58, 60, 61, 62, 65], "branches": [[57, 58], [57, 60], [60, 61], [60, 65], [61, 60], [61, 62]]}
# gained: {"lines": [22, 48, 57, 58, 60, 61, 62, 65], "branches": [[57, 58], [57, 60], [60, 61], [61, 60], [61, 62]]}

import pytest
from httpie.utils import humanize_bytes

def test_humanize_bytes_1_byte():
    assert humanize_bytes(1) == '1 B'

def test_humanize_bytes_kilobytes():
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'

def test_humanize_bytes_megabytes():
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'

def test_humanize_bytes_gigabytes():
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'

def test_humanize_bytes_terabytes():
    assert humanize_bytes(1 << 40, precision=2) == '1.00 TB'

def test_humanize_bytes_petabytes():
    assert humanize_bytes(1 << 50, precision=2) == '1.00 PB'
