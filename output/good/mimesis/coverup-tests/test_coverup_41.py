# file mimesis/providers/internet.py:171-181
# lines [171, 172, 173, 180, 181]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_image_placeholder_default_size():
    internet = Internet()
    default_image_url = internet.image_placeholder()
    assert default_image_url == 'http://placehold.it/1920x1080'

def test_image_placeholder_custom_size():
    internet = Internet()
    custom_width = 300
    custom_height = 250
    custom_image_url = internet.image_placeholder(width=custom_width, height=custom_height)
    assert custom_image_url == f'http://placehold.it/{custom_width}x{custom_height}'

def test_image_placeholder_string_size():
    internet = Internet()
    string_width = '450'
    string_height = '350'
    string_image_url = internet.image_placeholder(width=string_width, height=string_height)
    assert string_image_url == f'http://placehold.it/{string_width}x{string_height}'
