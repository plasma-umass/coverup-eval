# file tornado/log.py:116-162
# lines [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162]
# branches ['143->144', '143->162', '144->145', '144->158', '147->151', '147->154', '158->159', '158->160']

import logging
import pytest
from unittest.mock import patch, MagicMock
from tornado.log import LogFormatter

# Constants used in LogFormatter
DEFAULT_FORMAT = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
DEFAULT_DATE_FORMAT = '%y%m%d %H:%M:%S'
DEFAULT_COLORS = {
    logging.DEBUG: 4,  # Blue
    logging.INFO: 2,  # Green
    logging.WARNING: 3,  # Yellow
    logging.ERROR: 1,  # Red
    logging.CRITICAL: 1,  # Red
}

# Test function to improve coverage
@pytest.fixture
def mock_curses_module(mocker):
    # Fixture to mock the curses module for the duration of the test
    mock_curses = MagicMock()
    mocker.patch('tornado.log.curses', new=mock_curses)
    return mock_curses

@pytest.mark.parametrize("color", [True, False])
def test_log_formatter_colors(color, mock_curses_module):
    with patch('tornado.log._stderr_supports_color', return_value=color):
        if color:
            # Mocking curses module to simulate color support
            mock_curses_module.tigetstr.side_effect = lambda cap: b"\033[m" if cap == "sgr0" else b""
            mock_curses_module.tparm.side_effect = lambda cap, _: b"\033[2;3%dm" % DEFAULT_COLORS[logging.ERROR]
            formatter = LogFormatter(color=color)
            assert formatter._colors[logging.ERROR] == "\033[2;3%dm" % DEFAULT_COLORS[logging.ERROR]
            assert formatter._normal == "\033[m"
        else:
            # Test without color support
            formatter = LogFormatter(color=color)
            assert formatter._colors == {}
            assert formatter._normal == ""
