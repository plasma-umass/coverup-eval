# file: lib/ansible/module_utils/common/text/formatters.py:99-114
# asked: {"lines": [112], "branches": [[105, 109], [109, 112]]}
# gained: {"lines": [112], "branches": [[109, 112]]}

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

SIZE_RANGES = {'Y': 1 << 80, 'Z': 1 << 70, 'E': 1 << 60, 'P': 1 << 50, 'T': 1 << 40, 'G': 1 << 30, 'M': 1 << 20, 'K': 1 << 10, 'B': 1}

def test_bytes_to_human_no_unit():
    # This test will cover the branch where unit is None and size >= limit
    size = 1 << 30  # 1 GiB
    result = bytes_to_human(size)
    assert result == '1.00 GB'

def test_bytes_to_human_with_unit():
    # This test will cover the branch where unit is not None and unit.upper() == suffix[0]
    size = 1 << 30  # 1 GiB
    result = bytes_to_human(size, unit='G')
    assert result == '1.00 GB'

def test_bytes_to_human_limit_equals_one():
    # This test will cover the branch where limit == 1
    size = 1  # 1 Byte
    result = bytes_to_human(size)
    assert result == '1.00 Bytes'
