# file isort/format.py:32-41
# lines [32, 33, 34, 35, 36, 37, 38, 39, 41]
# branches ['34->35', '34->41', '35->36', '35->37']

import pytest

from isort.format import format_natural

def test_format_natural_without_from_or_import():
    # Test with a single word that should be prefixed with 'import '
    result = format_natural("os")
    assert result == "import os"

    # Test with a dotted path that should be converted to 'from ... import ...'
    result = format_natural("os.path.join")
    assert result == "from os.path import join"

def test_format_natural_with_from_or_import():
    # Test with a line that already starts with 'from '
    result = format_natural("from os import path")
    assert result == "from os import path"

    # Test with a line that already starts with 'import '
    result = format_natural("import os")
    assert result == "import os"
