# file mimesis/providers/internet.py:171-181
# lines [171, 172, 173, 180, 181]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_image_placeholder():
    internet = Internet()

    # Test with default parameters
    default_url = internet.image_placeholder()
    assert default_url == 'http://placehold.it/1920x1080'

    # Test with custom integer parameters
    custom_url = internet.image_placeholder(800, 600)
    assert custom_url == 'http://placehold.it/800x600'

    # Test with custom string parameters
    custom_str_url = internet.image_placeholder('1024', '768')
    assert custom_str_url == 'http://placehold.it/1024x768'

    # Test with mixed parameters
    mixed_url = internet.image_placeholder(500, '400')
    assert mixed_url == 'http://placehold.it/500x400'
