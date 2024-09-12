# file: tornado/log.py:261-339
# asked: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}
# gained: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}

import pytest
from unittest.mock import MagicMock, patch

def test_define_logging_options_with_default_options():
    with patch('tornado.options.options') as mock_options:
        mock_define = MagicMock()
        mock_options.define = mock_define
        from tornado.log import define_logging_options
        define_logging_options()
        assert mock_define.call_count == 8

def test_define_logging_options_with_custom_options():
    mock_options = MagicMock()
    from tornado.log import define_logging_options
    define_logging_options(mock_options)
    assert mock_options.define.call_count == 8

    # Check if the correct options are defined
    mock_options.define.assert_any_call(
        "logging",
        default="info",
        help="Set the Python log level. If 'none', tornado won't touch the logging configuration.",
        metavar="debug|info|warning|error|none",
    )
    mock_options.define.assert_any_call(
        "log_to_stderr",
        type=bool,
        default=None,
        help="Send log output to stderr (colorized if possible). By default use stderr if --log_file_prefix is not set and no other logging is configured.",
    )
    mock_options.define.assert_any_call(
        "log_file_prefix",
        type=str,
        default=None,
        metavar="PATH",
        help="Path prefix for log files. Note that if you are running multiple tornado processes, log_file_prefix must be different for each of them (e.g. include the port number)",
    )
    mock_options.define.assert_any_call(
        "log_file_max_size",
        type=int,
        default=100 * 1000 * 1000,
        help="max size of log files before rollover",
    )
    mock_options.define.assert_any_call(
        "log_file_num_backups", type=int, default=10, help="number of log files to keep"
    )
    mock_options.define.assert_any_call(
        "log_rotate_when",
        type=str,
        default="midnight",
        help="specify the type of TimedRotatingFileHandler interval other options:('S', 'M', 'H', 'D', 'W0'-'W6')",
    )
    mock_options.define.assert_any_call(
        "log_rotate_interval",
        type=int,
        default=1,
        help="The interval value of timed rotating",
    )
    mock_options.define.assert_any_call(
        "log_rotate_mode",
        type=str,
        default="size",
        help="The mode of rotating files(time or size)",
    )

    # Check if the parse callback is added
    assert mock_options.add_parse_callback.call_count == 1
