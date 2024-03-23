# file lib/ansible/executor/interpreter_discovery.py:181-202
# lines [181, 183, 184, 185, 187, 189, 192, 194, 197, 202]
# branches ['184->185', '184->187', '194->197', '194->202']

import pytest
from distutils.version import LooseVersion
import bisect

# Assuming the _version_fuzzy_match function is part of a module, we need to import it correctly
# For the sake of this example, let's assume it's a standalone function in the module
from ansible.executor.interpreter_discovery import _version_fuzzy_match

@pytest.fixture
def version_map():
    return {
        "2.7": "python2.7",
        "3.5": "python3.5",
        "3.6": "python3.6",
        "3.7": "python3.7",
        "3.8": "python3.8",
    }

def test_version_fuzzy_match_exact(version_map):
    # Test exact match
    assert _version_fuzzy_match("3.6", version_map) == "python3.6"

def test_version_fuzzy_match_older_than_all(version_map):
    # Test version older than all in the list
    assert _version_fuzzy_match("2.6", version_map) == "python2.7"

def test_version_fuzzy_match_newer_than_all(version_map):
    # Test version newer than all in the list
    assert _version_fuzzy_match("3.9", version_map) == "python3.8"

def test_version_fuzzy_match_in_between(version_map):
    # Test version that is in between existing versions
    assert _version_fuzzy_match("3.5.1", version_map) == "python3.5"

# The following code is for running the tests with pytest, but should not be included in the response
# as per the instructions. It is commented out here for reference only.

# if __name__ == "__main__":
#     pytest.main([__file__])
