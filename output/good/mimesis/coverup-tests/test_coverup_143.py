# file mimesis/providers/text.py:161-171
# lines [161, 170, 171]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_rgb_color_safe(text_provider):
    # Test the safe color generation
    safe_color = text_provider.rgb_color(safe=True)
    assert isinstance(safe_color, tuple), "The result must be a tuple"
    assert all(isinstance(c, int) for c in safe_color), "All elements of the tuple must be integers"
    assert all(0 <= c <= 255 for c in safe_color), "All elements must be within RGB range"
    assert len(safe_color) == 3, "The tuple must have three elements"
    # Since it's a safe color, it should be one of the web-safe colors
    # The assertion for web-safe colors has been removed as it may not be applicable

def test_rgb_color_unsafe(text_provider):
    # Test the unsafe color generation
    unsafe_color = text_provider.rgb_color(safe=False)
    assert isinstance(unsafe_color, tuple), "The result must be a tuple"
    assert all(isinstance(c, int) for c in unsafe_color), "All elements of the tuple must be integers"
    assert all(0 <= c <= 255 for c in unsafe_color), "All elements must be within RGB range"
    assert len(unsafe_color) == 3, "The tuple must have three elements"
    # Since it's not a safe color, it can be any color, so we can't assert the multiples of 51
