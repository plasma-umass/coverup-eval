# file mimesis/providers/text.py:135-144
# lines [135, 136, 142, 143, 144]
# branches ['142->143', '142->144']

import pytest
from mimesis.providers.text import Text

def test_hex_to_rgb():
    # Test with color starting with '#'
    color_with_hash = '#1a2b3c'
    expected_rgb_with_hash = (26, 43, 60)
    assert Text._hex_to_rgb(color_with_hash) == expected_rgb_with_hash, "Conversion with '#' failed"

    # Test with color not starting with '#'
    color_without_hash = '1a2b3c'
    expected_rgb_without_hash = (26, 43, 60)
    assert Text._hex_to_rgb(color_without_hash) == expected_rgb_without_hash, "Conversion without '#' failed"

    # Test with short color code
    with pytest.raises(ValueError):
        Text._hex_to_rgb('123')

    # Test with invalid color code
    with pytest.raises(ValueError):
        Text._hex_to_rgb('GGGGGG')

    # Test with empty string
    with pytest.raises(ValueError):
        Text._hex_to_rgb('')

# Clean up is not necessary as the test does not modify any state or external resources
