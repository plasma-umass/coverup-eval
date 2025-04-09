# file: lib/ansible/module_utils/common/text/formatters.py:99-114
# asked: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114], "branches": [[101, 102], [101, 103], [105, 106], [105, 109], [106, 105], [106, 107], [109, 110], [109, 112]]}
# gained: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114], "branches": [[101, 102], [101, 103], [105, 106], [105, 109], [106, 105], [106, 107], [109, 110], [109, 112]]}

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

SIZE_RANGES = {'Y': 1 << 80, 'Z': 1 << 70, 'E': 1 << 60, 'P': 1 << 50, 'T': 1 << 40, 'G': 1 << 30, 'M': 1 << 20, 'K': 1 << 10, 'B': 1}

def test_bytes_to_human_bytes():
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(0) == '0.00 Bytes'

def test_bytes_to_human_bits():
    assert bytes_to_human(1024, isbits=True) == '1.00 Kb'
    assert bytes_to_human(1, isbits=True) == '1.00 bits'
    assert bytes_to_human(0, isbits=True) == '0.00 bits'

def test_bytes_to_human_with_unit():
    assert bytes_to_human(1024, unit='K') == '1.00 KB'
    assert bytes_to_human(1, unit='B') == '1.00 Bytes'
    assert bytes_to_human(1 << 30, unit='G') == '1.00 GB'
    assert bytes_to_human(1 << 30, unit='M') == '1024.00 MB'
