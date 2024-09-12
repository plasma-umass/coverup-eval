# file: tornado/options.py:154-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}

import pytest
from unittest.mock import MagicMock

from tornado.options import OptionParser, _Option

@pytest.fixture
def option_parser():
    parser = OptionParser()
    return parser

def test_setattr_recognized_option(option_parser):
    option = _Option(name="test_option", default=None, type=str)
    option_parser._options["test-option"] = option

    option_parser.__setattr__("test_option", "new_value")

    assert option_parser._options["test-option"].value() == "new_value"

def test_setattr_unrecognized_option(option_parser):
    with pytest.raises(AttributeError, match="Unrecognized option 'unrecognized-option'"):
        option_parser.__setattr__("unrecognized_option", "value")
