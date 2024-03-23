# file mimesis/providers/text.py:135-144
# lines [135, 136, 142, 143, 144]
# branches ['142->143', '142->144']

import pytest
from mimesis.providers.text import Text

def test_hex_to_rgb():
    # Test with color starting with '#'
    color_with_hash = '#ff00ff'
    expected_rgb_with_hash = (255, 0, 255)
    assert Text._hex_to_rgb(color_with_hash) == expected_rgb_with_hash

    # Test with color not starting with '#'
    color_without_hash = '00ff00'
    expected_rgb_without_hash = (0, 255, 0)
    assert Text._hex_to_rgb(color_without_hash) == expected_rgb_without_hash

    # Test with color in lowercase
    color_lowercase = 'abcdef'
    expected_rgb_lowercase = (171, 205, 239)
    assert Text._hex_to_rgb(color_lowercase) == expected_rgb_lowercase

    # Test with color in uppercase
    color_uppercase = 'ABCDEF'
    expected_rgb_uppercase = (171, 205, 239)
    assert Text._hex_to_rgb(color_uppercase) == expected_rgb_uppercase

    # Test with short color
    with pytest.raises(ValueError):
        Text._hex_to_rgb('fff')

    # Test with invalid color
    with pytest.raises(ValueError):
        Text._hex_to_rgb('gggggg')
