# file tornado/log.py:261-339
# lines [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339]
# branches ['270->272', '270->275']

import pytest
from unittest import mock
from tornado.options import OptionParser

# Import the function to be tested
from tornado.log import define_logging_options

def test_define_logging_options(mocker):
    # Create a mock OptionParser instance
    mock_options = OptionParser()

    # Mock the enable_pretty_logging function
    mock_enable_pretty_logging = mocker.patch('tornado.log.enable_pretty_logging')

    # Call the function with the mock options
    define_logging_options(mock_options)

    # Check that the options were defined correctly
    assert mock_options.logging == "info"
    assert mock_options.log_to_stderr is None
    assert mock_options.log_file_prefix is None
    assert mock_options.log_file_max_size == 100 * 1000 * 1000
    assert mock_options.log_file_num_backups == 10
    assert mock_options.log_rotate_when == "midnight"
    assert mock_options.log_rotate_interval == 1
    assert mock_options.log_rotate_mode == "size"

    # Check that the parse callback was added and called
    mock_options._parse_callbacks[0]()
    mock_enable_pretty_logging.assert_called_once_with(mock_options)

def test_define_logging_options_default(mocker):
    # Mock the tornado.options.options
    mock_options = mocker.patch('tornado.options.options', new_callable=OptionParser)

    # Mock the enable_pretty_logging function
    mock_enable_pretty_logging = mocker.patch('tornado.log.enable_pretty_logging')

    # Call the function without passing options
    define_logging_options()

    # Check that the options were defined correctly
    assert mock_options.logging == "info"
    assert mock_options.log_to_stderr is None
    assert mock_options.log_file_prefix is None
    assert mock_options.log_file_max_size == 100 * 1000 * 1000
    assert mock_options.log_file_num_backups == 10
    assert mock_options.log_rotate_when == "midnight"
    assert mock_options.log_rotate_interval == 1
    assert mock_options.log_rotate_mode == "size"

    # Check that the parse callback was added and called
    mock_options._parse_callbacks[0]()
    mock_enable_pretty_logging.assert_called_once_with(mock_options)
