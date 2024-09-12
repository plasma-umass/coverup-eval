# file: f066/__init__.py:1-3
# asked: {"lines": [1, 2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [1, 2, 3], "branches": [[2, 2], [2, 3]]}

import pytest
from f066 import digitSum

def test_digitSum_empty_string():
    assert digitSum('') == 0

def test_digitSum_all_uppercase(monkeypatch):
    assert digitSum('ABC') == ord('A') + ord('B') + ord('C')

def test_digitSum_mixed_case(monkeypatch):
    assert digitSum('aBc') == ord('B')

def test_digitSum_no_uppercase(monkeypatch):
    assert digitSum('abc') == 0
