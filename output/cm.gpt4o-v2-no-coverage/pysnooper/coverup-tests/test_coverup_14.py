# file: pysnooper/utils.py:81-87
# asked: {"lines": [81, 82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [81, 82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest
from pysnooper.utils import truncate

def test_truncate_no_max_length():
    assert truncate("hello world", None) == "hello world"

def test_truncate_shorter_than_max_length():
    assert truncate("hello", 10) == "hello"

def test_truncate_equal_to_max_length():
    assert truncate("hello", 5) == "hello"

def test_truncate_longer_than_max_length():
    assert truncate("hello world", 5) == "h...d"

def test_truncate_edge_case():
    assert truncate("hello world", 11) == "hello world"
    assert truncate("hello world", 10) == "hel...orld"
