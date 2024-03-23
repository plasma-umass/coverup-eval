# file mimesis/providers/internet.py:43-46
# lines [43, 44, 46]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_internet_meta():
    internet_provider = Internet()
    assert internet_provider.Meta.name == 'internet'
