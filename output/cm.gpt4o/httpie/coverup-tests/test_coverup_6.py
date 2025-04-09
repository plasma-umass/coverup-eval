# file httpie/output/formatters/colors.py:207-256
# lines [207, 208, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
# branches []

import pytest
from pygments.style import Style
from pygments.token import Keyword, Name, String

def test_solarized256style():
    from httpie.output.formatters.colors import Solarized256Style

    # Check if Solarized256Style is a subclass of pygments.style.Style
    assert issubclass(Solarized256Style, Style)

    # Check if the background color is set correctly
    assert Solarized256Style.background_color == Solarized256Style.BASE03

    # Check if the styles dictionary contains the expected tokens and colors
    expected_styles = {
        Keyword: Solarized256Style.GREEN,
        Keyword.Constant: Solarized256Style.ORANGE,
        Keyword.Declaration: Solarized256Style.BLUE,
        Keyword.Namespace: Solarized256Style.ORANGE,
        Keyword.Reserved: Solarized256Style.BLUE,
        Keyword.Type: Solarized256Style.RED,
        Name.Attribute: Solarized256Style.BASE1,
        Name.Builtin: Solarized256Style.BLUE,
        Name.Builtin.Pseudo: Solarized256Style.BLUE,
        Name.Class: Solarized256Style.BLUE,
        Name.Constant: Solarized256Style.ORANGE,
        Name.Decorator: Solarized256Style.BLUE,
        Name.Entity: Solarized256Style.ORANGE,
        Name.Exception: Solarized256Style.YELLOW,
        Name.Function: Solarized256Style.BLUE,
        Name.Tag: Solarized256Style.BLUE,
        Name.Variable: Solarized256Style.BLUE,
        String: Solarized256Style.CYAN,
        String.Backtick: Solarized256Style.BASE01,
        String.Char: Solarized256Style.CYAN,
    }

    for token, color in expected_styles.items():
        assert Solarized256Style.styles[token] == color
