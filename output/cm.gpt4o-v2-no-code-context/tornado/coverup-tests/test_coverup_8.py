# file: tornado/log.py:261-339
# asked: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}
# gained: {"lines": [261, 270, 272, 274, 275, 276, 277, 279, 282, 284, 285, 286, 287, 289, 294, 295, 296, 297, 298, 300, 306, 307, 308, 309, 310, 312, 313, 316, 317, 318, 319, 321, 325, 326, 327, 328, 329, 332, 333, 334, 335, 336, 339], "branches": [[270, 272], [270, 275]]}

import pytest
from unittest import mock
from tornado.log import define_logging_options
from tornado.options import OptionParser, Error

@pytest.fixture
def mock_options():
    return OptionParser()

def test_define_logging_options_with_default_options(monkeypatch):
    import tornado.options
    mock_options_instance = OptionParser()

    with mock.patch('tornado.options.options', mock_options_instance):
        define_logging_options()
        assert mock_options_instance.logging == 'info'
        assert mock_options_instance.log_to_stderr is None
        assert mock_options_instance.log_file_prefix is None
        assert mock_options_instance.log_file_max_size == 100 * 1000 * 1000
        assert mock_options_instance.log_file_num_backups == 10
        assert mock_options_instance.log_rotate_when == 'midnight'
        assert mock_options_instance.log_rotate_interval == 1
        assert mock_options_instance.log_rotate_mode == 'size'

def test_define_logging_options_with_custom_options(mock_options):
    define_logging_options(mock_options)
    assert mock_options.logging == 'info'
    assert mock_options.log_to_stderr is None
    assert mock_options.log_file_prefix is None
    assert mock_options.log_file_max_size == 100 * 1000 * 1000
    assert mock_options.log_file_num_backups == 10
    assert mock_options.log_rotate_when == 'midnight'
    assert mock_options.log_rotate_interval == 1
    assert mock_options.log_rotate_mode == 'size'

def test_define_logging_options_parse_callback(monkeypatch):
    import tornado.options
    mock_options_instance = OptionParser()

    with mock.patch('tornado.options.options', mock_options_instance):
        parse_callback = mock.Mock()
        monkeypatch.setattr('tornado.log.enable_pretty_logging', parse_callback)
        define_logging_options()
        mock_options_instance.run_parse_callbacks()
        parse_callback.assert_called_once_with(mock_options_instance)
