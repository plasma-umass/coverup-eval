# file lib/ansible/modules/pip.py:623-626
# lines [623, 624, 626]
# branches []

import pytest
import re

# Assuming the Package class is defined in ansible/modules/pip.py
from ansible.modules.pip import Package

@pytest.fixture
def mock_canonicalize_re(mocker):
    original_re = Package._CANONICALIZE_RE
    mocker.patch.object(Package, '_CANONICALIZE_RE', re.compile(r"[-_.]+"))
    yield
    Package._CANONICALIZE_RE = original_re

def test_canonicalize_name(mock_canonicalize_re):
    # Test cases for canonicalize_name
    test_cases = [
        ("example_name", "example-name"),
        ("example.name", "example-name"),
        ("example-name", "example-name"),
        ("Example_Name", "example-name"),
        ("EXAMPLE.NAME", "example-name"),
    ]

    for input_name, expected_output in test_cases:
        assert Package.canonicalize_name(input_name) == expected_output

