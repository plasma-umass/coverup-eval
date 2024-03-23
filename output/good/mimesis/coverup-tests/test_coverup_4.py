# file mimesis/providers/internet.py:220-236
# lines [220, 230, 231, 233, 234, 236]
# branches ['233->234', '233->236']

import pytest
from mimesis.providers.internet import Internet

# Mock HASHTAGS to ensure consistent test results
HASHTAGS = ['love', 'sky', 'nice']

@pytest.fixture
def internet_provider(mocker):
    mocker.patch('mimesis.providers.internet.HASHTAGS', HASHTAGS)
    return Internet()

def test_hashtags_single(internet_provider):
    hashtag = internet_provider.hashtags(quantity=1)
    assert hashtag in ['#love', '#sky', '#nice']

def test_hashtags_multiple(internet_provider):
    hashtags = internet_provider.hashtags(quantity=3)
    assert len(hashtags) == 3
    for tag in hashtags:
        assert tag in ['#love', '#sky', '#nice']
