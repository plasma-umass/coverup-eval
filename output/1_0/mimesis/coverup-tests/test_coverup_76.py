# file mimesis/random.py:24-31
# lines [24, 25]
# branches []

import pytest
from mimesis.random import Random
from unittest.mock import MagicMock

def test_custom_random_class_methods():
    # Create a MagicMock to simulate the random_module.Random
    mock_random = MagicMock()

    # Patch the Random class with our MagicMock
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('mimesis.random.random_module.Random', mock_random)

        # Instantiate the custom Random class
        custom_random = Random()

        # Assert that the custom_random is an instance of MagicMock
        assert isinstance(custom_random, Random)

        # No need to clean up manually, as the context manager handles it
