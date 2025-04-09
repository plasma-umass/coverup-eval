# file: pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest
from pysnooper.utils import truncate

def test_truncate_no_max_length():
    assert truncate("example", None) == "example"

def test_truncate_shorter_than_max_length():
    assert truncate("example", 10) == "example"

def test_truncate_equal_to_max_length():
    assert truncate("example", 7) == "example"

def test_truncate_longer_than_max_length():
    assert truncate("example", 5) == "e...e"

def test_truncate_edge_case():
    assert truncate("example", 4) == "...e"
