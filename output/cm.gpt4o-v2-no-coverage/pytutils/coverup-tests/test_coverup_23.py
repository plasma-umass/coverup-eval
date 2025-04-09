# file: pytutils/env.py:13-41
# asked: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 27], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}
# gained: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 27], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}

import pytest
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents_basic():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

def test_parse_env_file_contents_single_quoted():
    lines = [
        "SINGLE_QUOTED='single_quoted_value'"
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ('SINGLE_QUOTED', 'single_quoted_value')
    ]

def test_parse_env_file_contents_double_quoted():
    lines = [
        'DOUBLE_QUOTED="double_quoted_value"'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ('DOUBLE_QUOTED', 'double_quoted_value')
    ]

def test_parse_env_file_contents_escaped_double_quoted():
    lines = [
        'ESCAPED_DOUBLE_QUOTED="escaped_\\\\n_newline"'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ('ESCAPED_DOUBLE_QUOTED', 'escaped_\\n_newline')
    ]

def test_parse_env_file_contents_no_match():
    lines = [
        'INVALID LINE'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == []

