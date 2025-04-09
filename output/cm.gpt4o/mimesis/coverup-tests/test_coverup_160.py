# file mimesis/providers/internet.py:161-169
# lines [161, 169]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.data import EMOJI

def test_emoji(mocker):
    # Mock the random.choice method to control the output
    mocker.patch('mimesis.providers.base.random.choice', return_value=':kissing:')
    
    internet = Internet()
    emoji = internet.emoji()
    
    # Assert that the emoji method returns the expected value
    assert emoji == ':kissing:'
