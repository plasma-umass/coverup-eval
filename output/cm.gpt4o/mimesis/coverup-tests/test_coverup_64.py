# file mimesis/builtins/ru.py:20-23
# lines [20, 21, 23]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_russia_spec_provider_meta():
    provider = RussiaSpecProvider()
    assert provider.Meta.name == 'russia_provider'
