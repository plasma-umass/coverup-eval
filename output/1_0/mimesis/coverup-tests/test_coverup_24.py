# file mimesis/enums.py:136-143
# lines [136, 137, 142, 143]
# branches []

import pytest
from mimesis.enums import PrefixSign

def test_prefix_sign_enum():
    assert PrefixSign.POSITIVE.value == 'positive'
    assert PrefixSign.NEGATIVE.value == 'negative'
