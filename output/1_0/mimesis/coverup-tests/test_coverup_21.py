# file mimesis/enums.py:49-56
# lines [49, 50, 55, 56]
# branches []

import pytest
from mimesis.enums import TitleType

def test_title_type_enum():
    assert TitleType.TYPICAL.value == 'typical'
    assert TitleType.ACADEMIC.value == 'academic'
    assert isinstance(TitleType.TYPICAL, TitleType)
    assert isinstance(TitleType.ACADEMIC, TitleType)
