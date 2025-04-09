# file: pytutils/env.py:13-41
# asked: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 27], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}
# gained: {"lines": [13, 27, 28, 30, 31, 33, 34, 35, 37, 38, 39, 41], "branches": [[27, 0], [27, 28], [30, 31], [34, 35], [34, 37], [38, 39], [38, 41]]}

import pytest
from pytutils.env import parse_env_file_contents

def test_parse_env_file_contents_basic():
    lines = [
        "TEST=some_value",
        "THISIS=another_value",
        "YOLO=yet_another_value"
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ("TEST", "some_value"),
        ("THISIS", "another_value"),
        ("YOLO", "yet_another_value")
    ]

def test_parse_env_file_contents_single_quotes():
    lines = [
        "TEST='some_value'",
        "THISIS='another_value'",
        "YOLO='yet_another_value'"
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ("TEST", "some_value"),
        ("THISIS", "another_value"),
        ("YOLO", "yet_another_value")
    ]

def test_parse_env_file_contents_double_quotes():
    lines = [
        'TEST="some_value"',
        'THISIS="another_value"',
        'YOLO="yet_another_value"'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ("TEST", "some_value"),
        ("THISIS", "another_value"),
        ("YOLO", "yet_another_value")
    ]

def test_parse_env_file_contents_escaped_double_quotes():
    lines = [
        r'TEST="some_\"escaped\"_value"',
        r'THISIS="another_\"escaped\"_value"',
        r'YOLO="yet_another_\"escaped\"_value"'
    ]
    result = list(parse_env_file_contents(lines))
    assert result == [
        ("TEST", 'some_"escaped"_value'),
        ("THISIS", 'another_"escaped"_value'),
        ("YOLO", 'yet_another_"escaped"_value')
    ]
