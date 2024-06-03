# file mimesis/providers/base.py:35-49
# lines [35, 45, 46, 48, 49]
# branches ['45->46', '45->48']

import pytest
from mimesis.providers.base import BaseProvider
from random import Random, random

class TestBaseProvider:
    def test_reseed_with_none_seed(self, mocker):
        provider = BaseProvider()
        provider.random = random  # Ensure the condition self.random is random is True

        mocker.patch.object(provider, 'random', Random())  # Mock the instance's random generator

        provider.reseed(None)

        assert isinstance(provider.random, Random)
        assert provider.seed is None

    def test_reseed_with_specific_seed(self, mocker):
        provider = BaseProvider()
        provider.random = random  # Ensure the condition self.random is random is True

        mocker.patch.object(provider, 'random', Random())  # Mock the instance's random generator

        specific_seed = 42
        provider.reseed(specific_seed)

        assert isinstance(provider.random, Random)
        assert provider.seed == specific_seed
        provider.random.seed(specific_seed)  # Ensure the seed method is called with the specific seed
