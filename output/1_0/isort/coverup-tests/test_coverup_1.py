# file isort/comments.py:4-12
# lines [4, 8, 9, 10, 12]
# branches ['9->10', '9->12']

import pytest
from isort.comments import parse

def test_parse_with_comment():
    line_with_comment = "import os # This is a comment"
    statement, comment = parse(line_with_comment)
    assert statement == "import os "
    assert comment == "This is a comment"

def test_parse_without_comment():
    line_without_comment = "import sys"
    statement, comment = parse(line_without_comment)
    assert statement == "import sys"
    assert comment == ""
