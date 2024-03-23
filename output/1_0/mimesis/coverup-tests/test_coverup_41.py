# file mimesis/providers/development.py:14-17
# lines [14, 15, 17]
# branches []

import pytest
from mimesis.providers.development import Development

def test_development_meta():
    development_provider = Development()
    assert development_provider.Meta.name == 'development'
