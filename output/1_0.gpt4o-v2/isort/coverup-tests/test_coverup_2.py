# file: isort/comments.py:15-32
# asked: {"lines": [15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30, 31, 32], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [29, 30], [29, 32], [30, 29], [30, 31]]}
# gained: {"lines": [15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30, 31, 32], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [29, 30], [29, 32], [30, 29], [30, 31]]}

import pytest
from isort.comments import add_to_line

def parse(string):
    # Mocking the parse function used in add_to_line
    return [string]

def test_add_to_line_no_comments():
    result = add_to_line(comments=None, original_string="test_string")
    assert result == "test_string"

def test_add_to_line_removed():
    result = add_to_line(comments=["comment1"], original_string="test_string", removed=True)
    assert result == "test_string"

def test_add_to_line_with_comments():
    result = add_to_line(comments=["comment1", "comment2"], original_string="test_string")
    assert result == "test_string comment1; comment2"

def test_add_to_line_with_duplicate_comments():
    result = add_to_line(comments=["comment1", "comment1"], original_string="test_string")
    assert result == "test_string comment1"

def test_add_to_line_with_comment_prefix():
    result = add_to_line(comments=["comment1"], original_string="test_string", comment_prefix="#")
    assert result == "test_string# comment1"

@pytest.fixture(autouse=True)
def mock_parse(monkeypatch):
    monkeypatch.setattr("isort.comments.parse", parse)
