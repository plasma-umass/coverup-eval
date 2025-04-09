# file tornado/options.py:710-715
# lines [715]
# branches []

import pytest
from tornado.options import OptionParser, options

def test_parse_config_file_executes_line_715(mocker):
    mocker.patch.object(OptionParser, 'parse_config_file', return_value=None)
    
    from tornado.options import parse_config_file
    
    test_path = "test_config.cfg"
    parse_config_file(test_path, final=True)
    
    OptionParser.parse_config_file.assert_called_once_with(test_path, final=True)
