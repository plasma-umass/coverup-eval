# file: lib/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_parse_with_integers():
    version = LooseVersion("1.2.3")
    version.parse("1.2.3")
    assert version.vstring == "1.2.3"
    assert version.version == [1, 2, 3]

def test_loose_version_parse_with_mixed():
    version = LooseVersion("1.2a.3")
    version.parse("1.2a.3")
    assert version.vstring == "1.2a.3"
    assert version.version == [1, 2, 'a', 3]

def test_loose_version_parse_with_non_numeric():
    version = LooseVersion("1.a.3")
    version.parse("1.a.3")
    assert version.vstring == "1.a.3"
    assert version.version == [1, 'a', 3]

def test_loose_version_parse_with_empty_string():
    version = LooseVersion("")
    version.parse("")
    assert version.vstring == ""
    assert version.version == []

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Ensure no state pollution
    yield
    # Teardown: Clean up any state if necessary
    monkeypatch.undo()
