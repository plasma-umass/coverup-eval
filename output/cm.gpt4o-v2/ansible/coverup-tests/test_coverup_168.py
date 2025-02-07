# file: lib/ansible/module_utils/common/text/formatters.py:99-114
# asked: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114], "branches": [[101, 102], [101, 103], [105, 106], [105, 109], [106, 105], [106, 107], [109, 110], [109, 112]]}
# gained: {"lines": [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 114], "branches": [[101, 102], [101, 103], [105, 106], [106, 105], [106, 107], [109, 110]]}

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

SIZE_RANGES = {'Y': 1 << 80, 'Z': 1 << 70, 'E': 1 << 60, 'P': 1 << 50, 'T': 1 << 40, 'G': 1 << 30, 'M': 1 << 20, 'K': 1 << 10, 'B': 1}

def test_bytes_to_human_bytes():
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1073741824) == '1.00 GB'
    assert bytes_to_human(1099511627776) == '1.00 TB'
    assert bytes_to_human(1125899906842624) == '1.00 PB'
    assert bytes_to_human(1152921504606846976) == '1.00 EB'
    assert bytes_to_human(1180591620717411303424) == '1.00 ZB'
    assert bytes_to_human(1208925819614629174706176) == '1.00 YB'

def test_bytes_to_human_bits():
    assert bytes_to_human(1024, isbits=True) == '1.00 Kb'
    assert bytes_to_human(1048576, isbits=True) == '1.00 Mb'
    assert bytes_to_human(1073741824, isbits=True) == '1.00 Gb'
    assert bytes_to_human(1099511627776, isbits=True) == '1.00 Tb'
    assert bytes_to_human(1125899906842624, isbits=True) == '1.00 Pb'
    assert bytes_to_human(1152921504606846976, isbits=True) == '1.00 Eb'
    assert bytes_to_human(1180591620717411303424, isbits=True) == '1.00 Zb'
    assert bytes_to_human(1208925819614629174706176, isbits=True) == '1.00 Yb'

def test_bytes_to_human_specific_unit():
    assert bytes_to_human(1024, unit='K') == '1.00 KB'
    assert bytes_to_human(1048576, unit='M') == '1.00 MB'
    assert bytes_to_human(1073741824, unit='G') == '1.00 GB'
    assert bytes_to_human(1099511627776, unit='T') == '1.00 TB'
    assert bytes_to_human(1125899906842624, unit='P') == '1.00 PB'
    assert bytes_to_human(1152921504606846976, unit='E') == '1.00 EB'
    assert bytes_to_human(1180591620717411303424, unit='Z') == '1.00 ZB'
    assert bytes_to_human(1208925819614629174706176, unit='Y') == '1.00 YB'
