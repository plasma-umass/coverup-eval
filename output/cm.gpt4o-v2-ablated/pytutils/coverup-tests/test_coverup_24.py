# file: pytutils/env.py:13-41
# asked: {"lines": [35, 39], "branches": [[30, 27], [34, 35], [38, 39]]}
# gained: {"lines": [35, 39], "branches": [[34, 35], [38, 39]]}

import pytest
import re
import typing
from collections import OrderedDict
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents(monkeypatch):
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        "SINGLE_QUOTED='single_quoted_value'",
        'DOUBLE_QUOTED="double_quoted_value"',
        'ESCAPED_DOUBLE_QUOTED="escaped\\_double\\_quoted_value"',
        'NO_QUOTES=no_quotes_value'
    ]
    
    expected_output = [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
        ('SINGLE_QUOTED', 'single_quoted_value'),
        ('DOUBLE_QUOTED', 'double_quoted_value'),
        ('ESCAPED_DOUBLE_QUOTED', 'escaped_double_quoted_value'),
        ('NO_QUOTES', 'no_quotes_value')
    ]
    
    result = list(parse_env_file_contents(lines))
    assert result == expected_output

    # Clean up any environment changes if necessary
    monkeypatch.undo()
