# file mimesis/providers/person.py:277-289
# lines [277, 278, 286, 287, 288, 289]
# branches []

import pytest
from mimesis.providers import Person
from mimesis.enums import SocialNetwork

@pytest.fixture
def person():
    return Person()

def test_social_media_profile(person, mocker):
    # Mock the username method to return a predictable username
    mocker.patch.object(person, 'username', return_value='test_user')

    # Test with a specific social network
    profile = person.social_media_profile(SocialNetwork.FACEBOOK)
    assert profile == 'https://facebook.com/test_user'

    # Test with another specific social network
    profile = person.social_media_profile(SocialNetwork.TWITTER)
    assert profile == 'https://twitter.com/test_user'

    # Test with a random social network
    profile = person.social_media_profile()
    assert profile.startswith('https://')
    assert 'test_user' in profile
