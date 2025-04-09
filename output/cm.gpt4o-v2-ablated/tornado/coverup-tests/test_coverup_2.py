# file: tornado/log.py:261-339
# asked: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}
# gained: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}

import pytest
from unittest import mock
from tornado.options import OptionParser

# Import the function to be tested
from tornado.log import define_logging_options

def test_define_logging_options_with_default_options(monkeypatch):
    # Mock the tornado.options.options to avoid state pollution
    mock_options = OptionParser()
    monkeypatch.setattr("tornado.options.options", mock_options)

    # Call the function with default options
    define_logging_options()

    # Assertions to verify that options were defined correctly
    assert mock_options.logging == "info"
    assert mock_options.log_to_stderr is None
    assert mock_options.log_file_prefix is None
    assert mock_options.log_file_max_size == 100 * 1000 * 1000
    assert mock_options.log_file_num_backups == 10
    assert mock_options.log_rotate_when == "midnight"
    assert mock_options.log_rotate_interval == 1
    assert mock_options.log_rotate_mode == "size"

def test_define_logging_options_with_custom_options():
    # Create a custom OptionParser instance
    custom_options = OptionParser()

    # Call the function with custom options
    define_logging_options(custom_options)

    # Assertions to verify that options were defined correctly
    assert custom_options.logging == "info"
    assert custom_options.log_to_stderr is None
    assert custom_options.log_file_prefix is None
    assert custom_options.log_file_max_size == 100 * 1000 * 1000
    assert custom_options.log_file_num_backups == 10
    assert custom_options.log_rotate_when == "midnight"
    assert custom_options.log_rotate_interval == 1
    assert custom_options.log_rotate_mode == "size"

def test_define_logging_options_parse_callback(monkeypatch):
    # Mock the tornado.options.options to avoid state pollution
    mock_options = OptionParser()
    monkeypatch.setattr("tornado.options.options", mock_options)

    # Mock the enable_pretty_logging function
    with mock.patch("tornado.log.enable_pretty_logging") as mock_enable_pretty_logging:
        # Call the function with default options
        define_logging_options()

        # Trigger the parse callback
        mock_options.run_parse_callbacks()

        # Assert that enable_pretty_logging was called
        mock_enable_pretty_logging.assert_called_once_with(mock_options)
