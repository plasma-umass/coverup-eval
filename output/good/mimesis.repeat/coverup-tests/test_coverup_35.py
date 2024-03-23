# file mimesis/providers/internet.py:171-181
# lines [171, 172, 173, 180, 181]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.mark.parametrize("width, height", [
    (300, 200),
    ('300', '200'),
    (300, '200'),
    ('300', 200),
])
def test_image_placeholder(width, height):
    internet = Internet()
    result = internet.image_placeholder(width, height)
    expected_url = f'http://placehold.it/{width}x{height}'
    assert result == expected_url
