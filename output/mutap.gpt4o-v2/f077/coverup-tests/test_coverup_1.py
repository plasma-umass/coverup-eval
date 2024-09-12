# file: f077/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f077 import iscube

def test_iscube_positive():
    assert iscube(27) == True

def test_iscube_negative():
    assert iscube(-27) == True

def test_iscube_non_cube():
    assert iscube(28) == False

def test_iscube_zero():
    assert iscube(0) == True
