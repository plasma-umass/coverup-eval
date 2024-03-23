# file mimesis/providers/base.py:35-49
# lines [35, 45, 46, 48, 49]
# branches ['45->46', '45->48']

import random
from mimesis.providers.base import BaseProvider
import pytest

class TestBaseProvider:
    @pytest.fixture
    def provider(self):
        return BaseProvider()

    def test_reseed_with_none(self, provider):
        # Save the original random module's state
        original_state = random.getstate()

        # Reseed with None, which should use the current system time
        provider.reseed(None)

        # Assert that the seed is set to None
        assert provider.seed is None

        # Assert that the provider's random is not the same as the random module
        assert provider.random is not random

        # Restore the original random module's state
        random.setstate(original_state)

    def test_reseed_with_specific_seed(self, provider):
        # Save the original random module's state
        original_state = random.getstate()

        # Reseed with a specific seed
        specific_seed = 12345
        provider.reseed(specific_seed)

        # Assert that the seed is set to the specific seed
        assert provider.seed == specific_seed

        # Assert that the provider's random is not the same as the random module
        assert provider.random is not random

        # Restore the original random module's state
        random.setstate(original_state)
