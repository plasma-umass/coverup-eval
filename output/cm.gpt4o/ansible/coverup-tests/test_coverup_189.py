# file lib/ansible/module_utils/common/text/formatters.py:99-114
# lines [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114]
# branches ['101->102', '101->103', '105->106', '105->109', '106->105', '106->107', '109->110', '109->112']

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

SIZE_RANGES = {
    'K': 1024,
    'M': 1024**2,
    'G': 1024**3,
    'T': 1024**4,
    'P': 1024**5,
    'E': 1024**6,
    'Z': 1024**7,
    'Y': 1024**8,
}

@pytest.mark.parametrize("size, isbits, unit, expected", [
    (1024, False, None, '1.00 KB'),
    (1024, True, None, '1.00 Kb'),
    (1024**2, False, None, '1.00 MB'),
    (1024**2, True, None, '1.00 Mb'),
    (1024**3, False, None, '1.00 GB'),
    (1024**3, True, None, '1.00 Gb'),
    (1024**4, False, None, '1.00 TB'),
    (1024**4, True, None, '1.00 Tb'),
    (1024**5, False, None, '1.00 PB'),
    (1024**5, True, None, '1.00 Pb'),
    (1024**6, False, None, '1.00 EB'),
    (1024**6, True, None, '1.00 Eb'),
    (1024**7, False, None, '1.00 ZB'),
    (1024**7, True, None, '1.00 Zb'),
    (1024**8, False, None, '1.00 YB'),
    (1024**8, True, None, '1.00 Yb'),
    (500, False, None, '500.00 Bytes'),
    (500, True, None, '500.00 bits'),
    (1024, False, 'K', '1.00 KB'),
    (1024, True, 'K', '1.00 Kb'),
    (1024**2, False, 'M', '1.00 MB'),
    (1024**2, True, 'M', '1.00 Mb'),
])
def test_bytes_to_human(size, isbits, unit, expected):
    assert bytes_to_human(size, isbits, unit) == expected
