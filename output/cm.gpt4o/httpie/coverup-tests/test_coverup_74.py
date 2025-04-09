# file httpie/output/formatters/colors.py:36-45
# lines [36, 37, 44]
# branches []

import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment
from httpie.plugins import FormatterPlugin

def test_color_formatter_initialization():
    env = Environment()
    formatter = ColorFormatter(env=env, format_options={})
    assert isinstance(formatter, FormatterPlugin)
    assert formatter.group_name == 'colors'
