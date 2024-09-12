# file: pysnooper/utils.py:81-87
# asked: {"lines": [81, 82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [81, 82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest
from pysnooper.utils import truncate

def test_truncate_no_max_length():
    assert truncate("hello world", None) == "hello world"

def test_truncate_short_string():
    assert truncate("short", 10) == "short"

def test_truncate_exact_length():
    assert truncate("exactly ten", 12) == "exactly ten"

def test_truncate_long_string():
    assert truncate("this is a very long string", 10) == "thi...ring"

def test_truncate_edge_case():
    assert truncate("edgecase", 5) == "e...e"
