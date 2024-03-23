# file pytutils/env.py:13-41
# lines [35, 39]
# branches ['30->27', '34->35', '38->39']

import pytest
import re
from collections import OrderedDict
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents():
    # Test to cover line 35
    lines = ["SINGLE_QUOTE='single_quote_value'"]
    result = OrderedDict(parse_env_file_contents(lines))
    assert result == {"SINGLE_QUOTE": "single_quote_value"}

    # Test to cover line 39
    lines = ['DOUBLE_QUOTE="double_quote_value"']
    result = OrderedDict(parse_env_file_contents(lines))
    assert result == {"DOUBLE_QUOTE": "double_quote_value"}

    # Test to cover branch 30->27 (no match)
    lines = ["# This is a comment", "   ", "INVALID_LINE"]
    result = OrderedDict(parse_env_file_contents(lines))
    assert result == {}

@pytest.fixture
def mock_environ(mocker):
    return mocker.patch.dict('os.environ', {}, clear=True)

def test_parse_env_file_contents_with_mock(mock_environ):
    # Use the mock_environ fixture to ensure a clean environment
    test_parse_env_file_contents()
