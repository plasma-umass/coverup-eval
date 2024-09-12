# file: isort/format.py:32-41
# asked: {"lines": [32, 33, 34, 35, 36, 37, 38, 39, 41], "branches": [[34, 35], [34, 41], [35, 36], [35, 37]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37, 38, 39, 41], "branches": [[34, 35], [34, 41], [35, 36], [35, 37]]}

import pytest
from isort.format import format_natural

def test_format_natural_with_leading_whitespace():
    assert format_natural("  import os") == "import os"

def test_format_natural_without_from_or_import():
    assert format_natural("os") == "import os"

def test_format_natural_with_dot_notation():
    assert format_natural("os.path") == "from os import path"

def test_format_natural_with_from_import():
    assert format_natural("from os import path") == "from os import path"

def test_format_natural_with_import():
    assert format_natural("import os") == "import os"
