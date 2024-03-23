# file mimesis/providers/text.py:161-171
# lines [170, 171]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_rgb_color_safe(text_provider):
    # Test the safe parameter branch
    safe_color = text_provider.rgb_color(safe=True)
    assert isinstance(safe_color, tuple), "The result must be a tuple"
    assert all(isinstance(c, int) for c in safe_color), "All elements of the tuple must be integers"
    assert all(0 <= c <= 255 for c in safe_color), "All elements must be within the range 0-255"
    # The assertion below is removed because the definition of "safe" colors is incorrect
    # assert safe_color in [(255, 255, 255), (0, 0, 0)], "Safe color must be either black or white"

def test_rgb_color_unsafe(text_provider):
    # Test the default behavior (unsafe)
    color = text_provider.rgb_color()
    assert isinstance(color, tuple), "The result must be a tuple"
    assert all(isinstance(c, int) for c in color), "All elements of the tuple must be integers"
    assert all(0 <= c <= 255 for c in color), "All elements must be within the range 0-255"
    # The assertion below is removed because there is no guarantee that an unsafe color is not black or white
    # assert color not in [(255, 255, 255), (0, 0, 0)], "Unsafe color should not be black or white"
