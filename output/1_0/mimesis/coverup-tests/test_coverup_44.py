# file mimesis/builtins/base.py:10-16
# lines [10, 11, 13, 15, 16]
# branches []

import pytest
from mimesis.builtins.base import BaseSpecProvider

def test_base_spec_provider_initialization():
    provider = BaseSpecProvider()
    assert provider._datafile == 'builtin.json'
