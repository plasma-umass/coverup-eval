# file mimesis/providers/internet.py:32-41
# lines [32, 38, 39, 40, 41]
# branches []

import pytest
from mimesis.providers import BaseProvider
from mimesis.providers import File
from mimesis.providers.internet import Internet

class TestInternet:
    @pytest.fixture
    def internet_provider(self):
        return Internet()

    def test_internet_init(self, internet_provider):
        assert isinstance(internet_provider, BaseProvider)
        assert isinstance(internet_provider._Internet__file, File)
        assert internet_provider._MAX_IPV4 == (2 ** 32) - 1
        assert internet_provider._MAX_IPV6 == (2 ** 128) - 1
