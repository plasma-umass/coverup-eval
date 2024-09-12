# file: isort/comments.py:4-12
# asked: {"lines": [4, 8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [4, 8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}

import pytest
from isort.comments import parse

def test_parse_with_comment():
    line = "import os  # This is a comment"
    import_statement, comment = parse(line)
    assert import_statement == "import os  "
    assert comment == "This is a comment"

def test_parse_without_comment():
    line = "import os"
    import_statement, comment = parse(line)
    assert import_statement == "import os"
    assert comment == ""

def test_parse_comment_at_start():
    line = "# This is a comment"
    import_statement, comment = parse(line)
    assert import_statement == ""
    assert comment == "This is a comment"

def test_parse_comment_at_end():
    line = "import os#"
    import_statement, comment = parse(line)
    assert import_statement == "import os"
    assert comment == ""
