# file mimesis/providers/base.py:35-49
# lines [35, 45, 46, 48, 49]
# branches ['45->46', '45->48']

import random
from mimesis.providers.base import BaseProvider
import pytest

class TestBaseProvider:
    def test_reseed_with_default_random(self):
        provider = BaseProvider()
        seed_value = 12345
        provider.reseed(seed_value)
        assert provider.seed == seed_value
        assert isinstance(provider.random, random.Random)
        # Check if the random object produces the same output for the same seed.
        provider.random.seed(seed_value)
        value1 = provider.random.random()
        random.seed(seed_value)
        value2 = random.random()
        assert value1 == value2

    def test_reseed_with_custom_random(self):
        provider = BaseProvider()
        provider.random = random.Random()
        seed_value = 67890
        provider.reseed(seed_value)
        assert provider.seed == seed_value
        # Check if the random object produces the same output for the same seed.
        provider.random.seed(seed_value)
        value1 = provider.random.random()
        new_random = random.Random()
        new_random.seed(seed_value)
        value2 = new_random.random()
        assert value1 == value2

# Run the tests
def test_reseed():
    test_instance = TestBaseProvider()
    test_instance.test_reseed_with_default_random()
    test_instance.test_reseed_with_custom_random()
