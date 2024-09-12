# file: pytutils/env.py:13-41
# asked: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 27], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}
# gained: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}

import pytest
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        "SINGLE_QUOTE='single_quote_value'",
        "DOUBLE_QUOTE=\"double_quote_value\"",
        "ESCAPED_DOUBLE_QUOTE=\"escaped\\\"_value\""
    ]
    
    expected_output = [
        ("TEST", "${HOME}/yeee"),
        ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"),
        ("SINGLE_QUOTE", "single_quote_value"),
        ("DOUBLE_QUOTE", "double_quote_value"),
        ("ESCAPED_DOUBLE_QUOTE", "escaped\"_value")
    ]
    
    result = list(parse_env_file_contents(lines))
    
    assert result == expected_output
