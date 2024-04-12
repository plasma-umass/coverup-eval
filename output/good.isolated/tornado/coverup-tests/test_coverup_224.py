# file tornado/options.py:154-158
# lines [155, 156, 157, 158]
# branches ['156->157', '156->158']

import pytest
from tornado.options import OptionParser, define, options

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    # Cleanup
    for name in list(options._options):
        options._options.pop(name, None)
    options._parse_callbacks.clear()

def test_setattr_raises_attribute_error(option_parser, mocker):
    define("test_option", default="default_value")
    with pytest.raises(AttributeError) as exc_info:
        option_parser.unrecognized_option = "value"
    assert "Unrecognized option" in str(exc_info.value)
