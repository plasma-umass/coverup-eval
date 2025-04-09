# file: pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode

def test_shitcode_ascii():
    result = shitcode("hello")
    assert result == "hello"

def test_shitcode_non_ascii():
    result = shitcode("hello世界")
    assert result == "hello??"

def test_shitcode_mixed():
    result = shitcode("hello世界123")
    assert result == "hello??123"
