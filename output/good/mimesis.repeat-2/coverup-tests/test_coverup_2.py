# file mimesis/providers/internet.py:220-236
# lines [220, 230, 231, 233, 234, 236]
# branches ['233->234', '233->236']

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_hashtags_single(internet_provider):
    hashtag = internet_provider.hashtags(quantity=1)
    assert isinstance(hashtag, str)
    assert hashtag.startswith('#')

def test_hashtags_multiple(internet_provider):
    quantity = 5
    hashtags = internet_provider.hashtags(quantity=quantity)
    assert isinstance(hashtags, list)
    assert len(hashtags) == quantity
    for tag in hashtags:
        assert isinstance(tag, str)
        assert tag.startswith('#')
