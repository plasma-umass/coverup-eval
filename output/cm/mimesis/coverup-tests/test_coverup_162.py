# file mimesis/providers/base.py:35-49
# lines []
# branches ['45->48']

import random
from mimesis.providers.base import BaseProvider
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def base_provider():
    return BaseProvider()

def test_reseed_with_default_random_module(mocker, base_provider):
    mocker.patch.object(base_provider, 'random', random.Random())
    base_provider.reseed(12345)
    assert base_provider.seed == 12345
    assert isinstance(base_provider.random, random.Random)
    assert base_provider.random is not random
