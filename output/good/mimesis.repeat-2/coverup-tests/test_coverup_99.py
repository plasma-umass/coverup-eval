# file mimesis/providers/person.py:277-289
# lines [277, 278, 286, 287, 288, 289]
# branches []

import pytest
from mimesis.enums import SocialNetwork
from mimesis.providers.person import Person

# Assuming SOCIAL_NETWORKS is a dictionary that maps SocialNetwork enum to URLs
SOCIAL_NETWORKS = {
    SocialNetwork.FACEBOOK: 'facebook.com/{}',
    SocialNetwork.TWITTER: 'twitter.com/{}',
    # Add other social networks as needed
    SocialNetwork.INSTAGRAM: 'instagram.com/{}',  # Added missing social network
}

# Mocking the username method to return a predictable username
@pytest.fixture
def person_with_mocked_username(mocker):
    mocker.patch('mimesis.providers.person.Person.username', return_value='test_user')
    return Person()

@pytest.mark.parametrize("social_network", [sn for sn in SocialNetwork if sn in SOCIAL_NETWORKS])
def test_social_media_profile(person_with_mocked_username, social_network):
    profile = person_with_mocked_username.social_media_profile(site=social_network)
    expected_url = 'https://' + SOCIAL_NETWORKS[social_network].format('test_user')
    assert profile == expected_url

def test_social_media_profile_without_site(person_with_mocked_username):
    profile = person_with_mocked_username.social_media_profile()
    assert profile.startswith('https://')
    assert 'test_user' in profile
