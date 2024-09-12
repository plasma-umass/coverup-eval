# file: pysnooper/utils.py:44-47
# asked: {"lines": [44, 45, 46], "branches": []}
# gained: {"lines": [44, 45, 46], "branches": []}

import pytest
from pysnooper.utils import shitcode

def test_shitcode_ascii():
    assert shitcode("hello") == "hello"

def test_shitcode_non_ascii():
    assert shitcode("hellö") == "hellö"

def test_shitcode_mixed():
    assert shitcode("hëllö") == "hëllö"

def test_shitcode_empty():
    assert shitcode("") == ""

def test_shitcode_special_chars():
    assert shitcode("!@#") == "!@#"

def test_shitcode_extended_ascii():
    assert shitcode("hell\x80") == "hell\x80"

