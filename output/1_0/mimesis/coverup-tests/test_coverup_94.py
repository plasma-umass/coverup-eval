# file mimesis/providers/development.py:82-87
# lines [82, 87]
# branches []

import pytest
from mimesis.providers.development import Development
from unittest.mock import patch

@pytest.fixture
def development_provider():
    return Development()

def test_boolean(development_provider):
    # Mock the random.choice method to control its output
    with patch.object(development_provider.random, 'choice', side_effect=[True, False]):
        assert development_provider.boolean() is True
        assert development_provider.boolean() is False
