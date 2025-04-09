# file: tornado/options.py:167-168
# asked: {"lines": [168], "branches": []}
# gained: {"lines": [168], "branches": []}

import pytest
from unittest.mock import MagicMock

from tornado.options import OptionParser, _Option

@pytest.fixture
def option_parser():
    parser = OptionParser()
    return parser

def test_getitem_existing_option(option_parser):
    option = _Option(name="test-option", default="default", type=str)
    option_parser._options["test-option"] = option
    option_parser._options["test-option"].value = MagicMock(return_value="mocked_value")

    assert option_parser["test-option"] == "mocked_value"
    option_parser._options["test-option"].value.assert_called_once()

def test_getitem_non_existing_option(option_parser):
    with pytest.raises(AttributeError, match="Unrecognized option 'non-existing-option'"):
        _ = option_parser["non-existing-option"]

def test_getitem_normalized_name(option_parser):
    option = _Option(name="test-option", default="default", type=str)
    option_parser._options["test-option"] = option
    option_parser._options["test-option"].value = MagicMock(return_value="mocked_value")

    assert option_parser["test_option"] == "mocked_value"
    option_parser._options["test-option"].value.assert_called_once()
