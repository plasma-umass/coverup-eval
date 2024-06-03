# file mimesis/providers/generic.py:71-84
# lines [71, 77, 78, 79, 80, 81, 82, 84]
# branches ['79->exit', '79->80']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseDataProvider

class MockBaseDataProvider(BaseDataProvider):
    def __init__(self, locale=None, seed=None):
        self._mock_method = self.mock_method
        self.locale = locale
        self.seed = seed

    def mock_method(self, locale, seed):
        return f"Locale: {locale}, Seed: {seed}"

@pytest.fixture
def mock_generic():
    class MockGeneric(Generic):
        def __init__(self, locale=None, seed=None):
            super().__init__(locale, seed)
            self._mock_method = MockBaseDataProvider().mock_method
    return MockGeneric(locale='en', seed=42)

def test_generic_getattr(mock_generic):
    result = mock_generic.mock_method
    assert result == "Locale: en, Seed: 42"
    assert 'mock_method' in mock_generic.__dict__
