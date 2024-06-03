# file docstring_parser/common.py:98-110
# lines [98, 99, 101, 108, 109, 110]
# branches []

import pytest
from docstring_parser.common import DocstringDeprecated

def test_docstring_deprecated_initialization():
    args = ["arg1", "arg2"]
    description = "This is a deprecated function."
    version = "1.0.0"
    
    deprecated = DocstringDeprecated(args, description, version)
    
    assert deprecated.args == args
    assert deprecated.description == description
    assert deprecated.version == version

@pytest.fixture(autouse=True)
def cleanup():
    # Perform any necessary cleanup here
    yield
    # Cleanup code to ensure no side effects
