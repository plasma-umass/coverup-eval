# file mimesis/enums.py:169-176
# lines [169, 170, 175, 176]
# branches []

import pytest
from mimesis.enums import EANFormat

def test_ean_format_enum():
    assert EANFormat.EAN8.value == 'ean-8'
    assert EANFormat.EAN13.value == 'ean-13'
