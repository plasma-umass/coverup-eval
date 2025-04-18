# file mimesis/providers/text.py:146-159
# lines [146, 155, 156, 158, 159]
# branches ['155->156', '155->158']

import pytest
from mimesis.providers.text import Text

SAFE_COLORS = [
    '#1abc9c', '#16a085', '#2ecc71', '#27ae60', '#3498db',
    '#2980b9', '#9b59b6', '#8e44ad', '#34495e', '#2c3e50',
    '#f1c40f', '#f39c12', '#e67e22', '#d35400', '#e74c3c',
    '#c0392b', '#ecf0f1', '#bdc3c7', '#95a5a6', '#7f8c8d',
]

@pytest.fixture
def text_provider():
    return Text()

def test_hex_color_safe(text_provider):
    color = text_provider.hex_color(safe=True)
    assert color in SAFE_COLORS

def test_hex_color_unsafe(text_provider):
    color = text_provider.hex_color(safe=False)
    assert color.startswith('#')
    assert len(color) == 7
    # Check if the color is a valid hex color
    int(color[1:], 16)
