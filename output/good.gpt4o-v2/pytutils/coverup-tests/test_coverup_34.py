# file: pytutils/env.py:13-41
# asked: {"lines": [], "branches": [[30, 27]]}
# gained: {"lines": [], "branches": [[30, 27]]}

import pytest
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents_unquoted():
    lines = ['UNQUOTED_VAR=value']
    result = list(parse_env_file_contents(lines))
    assert result == [('UNQUOTED_VAR', 'value')]

def test_parse_env_file_contents_single_quoted():
    lines = ["SINGLE_QUOTED_VAR='value'"]
    result = list(parse_env_file_contents(lines))
    assert result == [('SINGLE_QUOTED_VAR', 'value')]

def test_parse_env_file_contents_double_quoted():
    lines = ['DOUBLE_QUOTED_VAR="value"']
    result = list(parse_env_file_contents(lines))
    assert result == [('DOUBLE_QUOTED_VAR', 'value')]

def test_parse_env_file_contents_escaped_double_quoted():
    lines = ['ESCAPED_DOUBLE_QUOTED_VAR="val\\ue"']
    result = list(parse_env_file_contents(lines))
    assert result == [('ESCAPED_DOUBLE_QUOTED_VAR', 'value')]

def test_parse_env_file_contents_mixed():
    lines = [
        'UNQUOTED_VAR=value',
        "SINGLE_QUOTED_VAR='value'",
        'DOUBLE_QUOTED_VAR="value"',
        'ESCAPED_DOUBLE_QUOTED_VAR="val\\ue"'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ('UNQUOTED_VAR', 'value'),
        ('SINGLE_QUOTED_VAR', 'value'),
        ('DOUBLE_QUOTED_VAR', 'value'),
        ('ESCAPED_DOUBLE_QUOTED_VAR', 'value')
    ]

def test_parse_env_file_contents_no_match():
    lines = ['# This is a comment', '   ', 'INVALID LINE']
    result = list(parse_env_file_contents(lines))
    assert result == []
