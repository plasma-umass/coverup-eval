# file mimesis/providers/person.py:277-289
# lines [286, 287, 288, 289]
# branches []

import pytest
from mimesis.enums import SocialNetwork
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_social_media_profile_with_none_site(person, mocker):
    mocker.patch('mimesis.providers.person.Person.username', return_value='some_user')
    profile = person.social_media_profile(site=None)
    assert 'some_user' in profile
    assert profile.startswith('https://')

def test_social_media_profile_with_specific_site(person, mocker):
    mocker.patch('mimesis.providers.person.Person.username', return_value='specific_user')
    for site in SocialNetwork:
        profile = person.social_media_profile(site=site)
        assert 'specific_user' in profile
        assert profile.startswith('https://')
