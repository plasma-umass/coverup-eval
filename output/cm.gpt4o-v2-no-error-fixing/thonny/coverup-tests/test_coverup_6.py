# file: thonny/jedi_utils.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from thonny.jedi_utils import _using_older_jedi

class MockJedi:
    def __init__(self, version):
        self.__version__ = version

def test_using_older_jedi_with_old_version():
    jedi = MockJedi("0.14.1")
    assert _using_older_jedi(jedi) == True

def test_using_older_jedi_with_new_version():
    jedi = MockJedi("0.18.0")
    assert _using_older_jedi(jedi) == False

def test_using_older_jedi_with_edge_case_version():
    jedi = MockJedi("0.17.9")
    assert _using_older_jedi(jedi) == True

def test_using_older_jedi_with_non_matching_version():
    jedi = MockJedi("1.0.0")
    assert _using_older_jedi(jedi) == False
