# file httpie/output/formatters/colors.py:101-106
# lines [101, 102, 103, 104, 105, 106]
# branches []

import pytest
from httpie.output.formatters.colors import ColorFormatter
from pygments.styles import get_style_by_name
from pygments.style import Style
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import Solarized256Style

def test_get_style_class_valid_scheme(mocker):
    mocker.patch('pygments.styles.get_style_by_name', return_value=Style)
    style_class = ColorFormatter.get_style_class('monokai')
    assert style_class == Style

def test_get_style_class_invalid_scheme(mocker):
    mocker.patch('pygments.styles.get_style_by_name', side_effect=ClassNotFound)
    style_class = ColorFormatter.get_style_class('invalid_scheme')
    assert style_class == Solarized256Style
