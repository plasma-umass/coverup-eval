# file mimesis/providers/text.py:161-171
# lines [161, 170, 171]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_rgb_color_safe(text_provider):
    safe_color = text_provider.rgb_color(safe=True)
    assert isinstance(safe_color, tuple)
    assert len(safe_color) == 3
    assert all(isinstance(c, int) for c in safe_color)
    assert all(0 <= c <= 255 for c in safe_color)

def test_rgb_color_unsafe(text_provider):
    unsafe_color = text_provider.rgb_color(safe=False)
    assert isinstance(unsafe_color, tuple)
    assert len(unsafe_color) == 3
    assert all(isinstance(c, int) for c in unsafe_color)
    assert all(0 <= c <= 255 for c in unsafe_color)
