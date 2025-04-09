# file: lib/ansible/module_utils/common/text/formatters.py:99-114
# asked: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114], "branches": [[101, 102], [101, 103], [105, 106], [105, 109], [106, 105], [106, 107], [109, 110], [109, 112]]}
# gained: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114], "branches": [[101, 102], [101, 103], [105, 106], [106, 105], [106, 107], [109, 110], [109, 112]]}

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

SIZE_RANGES = {'Y': 1 << 80, 'Z': 1 << 70, 'E': 1 << 60, 'P': 1 << 50, 'T': 1 << 40, 'G': 1 << 30, 'M': 1 << 20, 'K': 1 << 10, 'B': 1}

@pytest.mark.parametrize("size, isbits, unit, expected", [
    (1 << 80, False, None, '1.00 YB'),
    (1 << 70, False, None, '1.00 ZB'),
    (1 << 60, False, None, '1.00 EB'),
    (1 << 50, False, None, '1.00 PB'),
    (1 << 40, False, None, '1.00 TB'),
    (1 << 30, False, None, '1.00 GB'),
    (1 << 20, False, None, '1.00 MB'),
    (1 << 10, False, None, '1.00 KB'),
    (1, False, None, '1.00 Bytes'),
    (1 << 80, True, None, '1.00 Yb'),
    (1 << 70, True, None, '1.00 Zb'),
    (1 << 60, True, None, '1.00 Eb'),
    (1 << 50, True, None, '1.00 Pb'),
    (1 << 40, True, None, '1.00 Tb'),
    (1 << 30, True, None, '1.00 Gb'),
    (1 << 20, True, None, '1.00 Mb'),
    (1 << 10, True, None, '1.00 Kb'),
    (1, True, None, '1.00 bits'),
    (1 << 80, False, 'Y', '1.00 YB'),
    (1 << 70, False, 'Z', '1.00 ZB'),
    (1 << 60, False, 'E', '1.00 EB'),
    (1 << 50, False, 'P', '1.00 PB'),
    (1 << 40, False, 'T', '1.00 TB'),
    (1 << 30, False, 'G', '1.00 GB'),
    (1 << 20, False, 'M', '1.00 MB'),
    (1 << 10, False, 'K', '1.00 KB'),
    (1, False, 'B', '1.00 Bytes'),
])
def test_bytes_to_human(size, isbits, unit, expected):
    assert bytes_to_human(size, isbits, unit) == expected
