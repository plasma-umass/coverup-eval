# file isort/comments.py:15-32
# lines [15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30, 31, 32]
# branches ['22->23', '22->25', '25->26', '25->28', '29->30', '29->32', '30->29', '30->31']

import pytest
from unittest.mock import patch

# Assuming the add_to_line function is defined in a module named isort.comments
# If the module name is different, replace 'isort.comments' with the correct module name

from isort.comments import add_to_line

def test_add_to_line_with_removed():
    with patch("isort.comments.parse", return_value=("code", "")):
        assert add_to_line(["# Comment"], "code # Comment", removed=True) == "code"

def test_add_to_line_without_comments():
    with patch("isort.comments.parse", return_value=("code", "")):
        assert add_to_line(None, "code") == "code"

def test_add_to_line_with_unique_comments():
    with patch("isort.comments.parse", return_value=("code", "")):
        comments = ["# Comment1", "# Comment2"]
        assert add_to_line(comments, "code", comment_prefix=" #") == "code # # Comment1; # Comment2"

def test_add_to_line_with_duplicate_comments():
    with patch("isort.comments.parse", return_value=("code", "")):
        comments = ["# Comment1", "# Comment1"]
        assert add_to_line(comments, "code", comment_prefix=" #") == "code # # Comment1"

def test_add_to_line_with_empty_original_string():
    with patch("isort.comments.parse", return_value=("", "")):
        comments = ["# Comment1"]
        assert add_to_line(comments, "", comment_prefix=" #") == " # # Comment1"

def test_add_to_line_with_no_comment_prefix():
    with patch("isort.comments.parse", return_value=("code", "")):
        comments = ["# Comment1"]
        assert add_to_line(comments, "code") == "code # Comment1"
