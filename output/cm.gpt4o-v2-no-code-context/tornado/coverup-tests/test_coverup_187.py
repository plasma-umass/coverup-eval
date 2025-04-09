# file: tornado/options.py:217-302
# asked: {"lines": [264, 265, 266, 277, 286, 288], "branches": [[263, 264], [273, 277], [283, 286], [287, 288]]}
# gained: {"lines": [264, 265, 266, 286, 288], "branches": [[263, 264], [283, 286], [287, 288]]}

import pytest
from tornado.options import OptionParser, Error

@pytest.fixture
def option_parser():
    return OptionParser()

def test_define_option_already_defined(option_parser):
    option_parser.define("test_option", default=1)
    with pytest.raises(Error, match="Option 'test-option' already defined in"):
        option_parser.define("test_option", default=2)

def test_define_with_callback(option_parser):
    callback_called = False

    def callback(value):
        nonlocal callback_called
        callback_called = True

    option_parser.define("test_option", default=1, callback=callback)
    option_parser._options["test-option"].set(2)
    assert callback_called

def test_define_without_type_and_default(option_parser):
    option_parser.define("test_option")
    assert option_parser._options["test-option"].type == str

def test_define_with_group(option_parser):
    option_parser.define("test_option", group="test_group")
    assert option_parser._options["test-option"].group_name == "test_group"

def test_define_with_multiple_and_no_default(option_parser):
    option_parser.define("test_option", multiple=True)
    assert option_parser._options["test-option"].type == str

def test_define_with_default_and_no_type(option_parser):
    option_parser.define("test_option", default=1)
    assert option_parser._options["test-option"].type == int
