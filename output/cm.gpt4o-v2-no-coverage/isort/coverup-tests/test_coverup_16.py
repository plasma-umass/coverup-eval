# file: isort/format.py:32-41
# asked: {"lines": [32, 33, 34, 35, 36, 37, 38, 39, 41], "branches": [[34, 35], [34, 41], [35, 36], [35, 37]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37, 38, 39, 41], "branches": [[34, 35], [34, 41], [35, 36], [35, 37]]}

import pytest
from isort.format import format_natural

def test_format_natural_import():
    assert format_natural("import os") == "import os"

def test_format_natural_from_import():
    assert format_natural("from os import path") == "from os import path"

def test_format_natural_no_prefix():
    assert format_natural("os") == "import os"

def test_format_natural_no_prefix_with_dot():
    assert format_natural("os.path") == "from os import path"

def test_format_natural_strip():
    assert format_natural("  import os  ") == "import os"

@pytest.mark.parametrize("input_str, expected", [
    ("import os", "import os"),
    ("from os import path", "from os import path"),
    ("os", "import os"),
    ("os.path", "from os import path"),
    ("  import os  ", "import os"),
])
def test_format_natural_parametrized(input_str, expected):
    assert format_natural(input_str) == expected
