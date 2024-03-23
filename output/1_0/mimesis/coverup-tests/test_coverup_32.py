# file mimesis/enums.py:179-188
# lines [179, 180, 185, 186, 187, 188]
# branches []

import pytest
from mimesis.enums import SocialNetwork

def test_social_network_enum():
    # Assert that all defined social networks are present
    assert SocialNetwork.FACEBOOK.value == 'facebook'
    assert SocialNetwork.TWITTER.value == 'twitter'
    assert SocialNetwork.INSTAGRAM.value == 'instagram'
    assert SocialNetwork.VK.value == 'vk'

    # Assert that the enum contains exactly four social networks
    assert len(SocialNetwork) == 4

    # Assert that the enum is iterable and items can be accessed
    for network in SocialNetwork:
        assert network in SocialNetwork
