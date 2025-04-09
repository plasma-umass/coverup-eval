# file tornado/options.py:217-302
# lines [264, 265, 266, 277, 286, 288]
# branches ['263->264', '273->277', '283->286', '287->288']

import pytest
from tornado.options import OptionParser, Error

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    parser._options.clear()

def test_define_option_already_defined(option_parser):
    option_parser.define("test_option", default=1)
    with pytest.raises(Error, match="Option 'test-option' already defined in"):
        option_parser.define("test_option", default=2)

def test_define_option_with_callback(option_parser, mocker):
    callback = mocker.Mock()
    option_parser.define("config", type=str, help="path to config file", callback=callback)
    option_parser._options["config"].callback("new_path")
    callback.assert_called_once_with("new_path")

def test_define_option_with_multiple_and_no_default(option_parser):
    option_parser.define("test_option", multiple=True)
    assert option_parser._options["test-option"].type == str

def test_define_option_with_group(option_parser):
    option_parser.define("test_option", group="test_group")
    assert option_parser._options["test-option"].group_name == "test_group"
