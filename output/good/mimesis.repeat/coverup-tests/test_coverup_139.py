# file mimesis/providers/internet.py:238-253
# lines [238, 247, 248, 249, 252, 253]
# branches []

import pytest
from mimesis.providers import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_home_page(internet_provider):
    home_page = internet_provider.home_page()
    assert home_page.startswith('https://')
    assert '.' in home_page
