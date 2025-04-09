# file: thonny/jedi_utils.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from thonny.jedi_utils import _using_older_jedi

def test_using_older_jedi():
    class MockJedi:
        def __init__(self, version):
            self.__version__ = version

    # Test cases for different versions
    versions_to_test = {
        "0.13.1": True,
        "0.14.2": True,
        "0.15.3": True,
        "0.16.4": True,
        "0.17.5": True,
        "0.18.0": False,
        "1.0.0": False,
        "0.12.0": False,
    }

    for version, expected in versions_to_test.items():
        jedi = MockJedi(version)
        assert _using_older_jedi(jedi) == expected
