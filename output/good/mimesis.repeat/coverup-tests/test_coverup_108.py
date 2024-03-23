# file mimesis/builtins/ru.py:12-14
# lines [12, 13]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

def test_russia_spec_provider_initialization():
    provider = RussiaSpecProvider()
    assert provider is not None
