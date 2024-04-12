# file httpie/output/formatters/colors.py:101-106
# lines [103, 104, 105, 106]
# branches []

import pytest
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import ColorFormatter
from pygments.style import Style

# Mock the pygments.styles.get_style_by_name function to raise ClassNotFound
@pytest.fixture
def mock_get_style_by_name(mocker):
    mocker.patch('pygments.styles.get_style_by_name', side_effect=ClassNotFound)

# Test function to cover lines 103-106
def test_get_style_class_with_invalid_color_scheme(mock_get_style_by_name):
    # Call the method with an invalid color scheme to trigger the exception
    style_class = ColorFormatter.get_style_class('invalid-color-scheme')
    
    # Assert that the fallback style class is returned
    assert issubclass(style_class, Style)
    # Since we cannot import Solarized256Style directly, we check for the name of the class
    assert style_class.__name__ == 'Solarized256Style'
