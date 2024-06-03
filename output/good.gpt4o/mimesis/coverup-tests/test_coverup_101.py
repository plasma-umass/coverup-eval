# file mimesis/providers/internet.py:43-46
# lines [43, 44, 46]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_internet_meta_name():
    internet = Internet()
    assert internet.Meta.name == 'internet'
