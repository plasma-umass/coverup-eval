# file isort/format.py:32-41
# lines [32, 33, 34, 35, 36, 37, 38, 39, 41]
# branches ['34->35', '34->41', '35->36', '35->37']

import pytest
from isort.format import format_natural

def test_format_natural():
    # Test case where import_line does not start with "from " or "import " and does not contain "."
    assert format_natural("os") == "import os"
    
    # Test case where import_line does not start with "from " or "import " and contains "."
    assert format_natural("os.path") == "from os import path"
    
    # Test case where import_line starts with "from "
    assert format_natural("from os import path") == "from os import path"
    
    # Test case where import_line starts with "import "
    assert format_natural("import os") == "import os"
    
    # Test case where import_line has leading and trailing spaces
    assert format_natural("  import os  ") == "import os"
