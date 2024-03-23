# file mimesis/enums.py:81-91
# lines [81, 82, 87, 88, 89, 90, 91]
# branches []

import pytest
from mimesis.enums import TLDType

def test_tldtype_enum():
    assert TLDType.CCTLD.value == 'cctld'
    assert TLDType.GTLD.value == 'gtld'
    assert TLDType.GEOTLD.value == 'geotld'
    assert TLDType.UTLD.value == 'utld'
    assert TLDType.STLD.value == 'stld'
