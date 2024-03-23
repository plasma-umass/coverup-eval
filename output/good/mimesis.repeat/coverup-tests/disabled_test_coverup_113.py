# file mimesis/providers/person.py:277-289
# lines [277, 278, 286, 287, 288, 289]
# branches []

import pytest
from mimesis.enums import SocialNetwork
from mimesis.providers.person import Person
from unittest.mock import patch

# Assuming the SOCIAL_NETWORKS dictionary is defined somewhere in the module
# If not, it should be defined for the purpose of this test
SOCIAL_NETWORKS = {
    SocialNetwork.FACEBOOK: 'facebook.com/{}',
    SocialNetwork.TWITTER: 'twitter.com/{}',
    SocialNetwork.INSTAGRAM: 'instagram.com/{}',
    # Add other social networks if they exist in the SocialNetwork enum
}

@pytest.fixture
def person():
    return Person()

@pytest.fixture
def username():
    return 'testuser'

def test_social_media_profile(person, username):
    with patch.object(Person, 'username', return_value=username):
        # Test with no site specified (should cover the default case)
        profile_default = person.social_media_profile()
        assert profile_default.startswith('https://')
        assert any(profile_default.startswith(f'https://{v.split("{")[0]}') for v in SOCIAL_NETWORKS.values())

        # Test with each specific site (should cover all branches)
        for site in SocialNetwork:
            if site in SOCIAL_NETWORKS:
                profile = person.social_media_profile(site=site)
                expected_url = 'https://' + SOCIAL_NETWORKS[site].format(username)
                assert profile == expected_url
