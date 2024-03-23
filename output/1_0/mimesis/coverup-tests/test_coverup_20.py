# file mimesis/providers/clothing.py:10-40
# lines [10, 11, 13, 14, 16, 18, 23, 26, 31, 33, 40]
# branches []

import pytest
from mimesis.providers.clothing import Clothing

@pytest.fixture
def clothing_provider():
    return Clothing()

def test_international_size(clothing_provider):
    size = clothing_provider.international_size()
    assert size in ['L', 'M', 'S', 'XL', 'XS', 'XXL', 'XXS', 'XXXL']

def test_european_size(clothing_provider):
    size = clothing_provider.european_size()
    assert 38 <= size <= 62

def test_custom_size(clothing_provider):
    min_size = 42
    max_size = 58
    size = clothing_provider.custom_size(minimum=min_size, maximum=max_size)
    assert min_size <= size <= max_size

def test_custom_size_default(clothing_provider):
    size = clothing_provider.custom_size()
    assert 40 <= size <= 62
