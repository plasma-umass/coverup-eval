# file mimesis/builtins/da.py:11-38
# lines [11, 12, 14, 16, 18, 19, 21, 23, 31, 32, 33, 34, 36, 38]
# branches []

import pytest
from mimesis.builtins.da import DenmarkSpecProvider

def test_cpr():
    provider = DenmarkSpecProvider()
    cpr_number = provider.cpr()
    assert len(cpr_number) == 10
    day, month, year, serial = int(cpr_number[:2]), int(cpr_number[2:4]), int(cpr_number[4:6]), int(cpr_number[6:])
    assert 1 <= day <= 31
    assert 1 <= month <= 12
    assert 0 <= year <= 99
    assert 0 <= serial <= 9999
