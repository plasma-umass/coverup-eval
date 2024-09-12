# file: lib/ansible/plugins/filter/core.py:460-461
# asked: {"lines": [460, 461], "branches": []}
# gained: {"lines": [460, 461], "branches": []}

import pytest
from ansible.plugins.filter.core import b64encode

def test_b64encode():
    # Test with a regular string
    result = b64encode("hello")
    assert result == "aGVsbG8=", f"Expected 'aGVsbG8=', but got {result}"

    # Test with an empty string
    result = b64encode("")
    assert result == "", f"Expected '', but got {result}"

    # Test with a string containing special characters
    result = b64encode("hello world!")
    assert result == "aGVsbG8gd29ybGQh", f"Expected 'aGVsbG8gd29ybGQh', but got {result}"

    # Test with a string containing non-ASCII characters
    result = b64encode("你好")
    assert result == "5L2g5aW9", f"Expected '5L2g5aW9', but got {result}"

    # Test with a different encoding
    result = b64encode("hello", encoding="ascii")
    assert result == "aGVsbG8=", f"Expected 'aGVsbG8=', but got {result}"

    # Test with a string that requires surrogateescape
    result = b64encode("hello\x80world", encoding="utf-8")
    assert result == "aGVsbG/CgHdvcmxk", f"Expected 'aGVsbG/CgHdvcmxk', but got {result}"
