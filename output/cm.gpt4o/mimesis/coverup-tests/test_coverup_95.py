# file mimesis/providers/text.py:161-171
# lines [161, 170, 171]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_rgb_color(text_provider):
    # Test with default parameter (safe=False)
    rgb = text_provider.rgb_color()
    assert isinstance(rgb, tuple)
    assert len(rgb) == 3
    assert all(isinstance(value, int) for value in rgb)
    assert all(0 <= value <= 255 for value in rgb)

    # Test with safe=True
    rgb_safe = text_provider.rgb_color(safe=True)
    assert isinstance(rgb_safe, tuple)
    assert len(rgb_safe) == 3
    assert all(isinstance(value, int) for value in rgb_safe)
    assert all(0 <= value <= 255 for value in rgb_safe)
