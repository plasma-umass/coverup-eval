# file mimesis/providers/text.py:135-144
# lines [135, 136, 142, 143, 144]
# branches ['142->143', '142->144']

import pytest
from mimesis.providers.text import Text

def test_hex_to_rgb():
    # Test with a hex color starting with '#'
    color_with_hash = "#ff5733"
    expected_rgb_with_hash = (255, 87, 51)
    assert Text._hex_to_rgb(color_with_hash) == expected_rgb_with_hash

    # Test with a hex color without '#'
    color_without_hash = "ff5733"
    expected_rgb_without_hash = (255, 87, 51)
    assert Text._hex_to_rgb(color_without_hash) == expected_rgb_without_hash

    # Test with a different hex color
    another_color = "#00ff00"
    expected_rgb_another = (0, 255, 0)
    assert Text._hex_to_rgb(another_color) == expected_rgb_another

    # Test with an invalid hex color (should raise ValueError)
    invalid_color = "zzzzzz"
    with pytest.raises(ValueError):
        Text._hex_to_rgb(invalid_color)
