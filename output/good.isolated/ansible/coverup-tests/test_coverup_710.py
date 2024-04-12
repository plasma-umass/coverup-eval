# file lib/ansible/module_utils/compat/version.py:101-139
# lines [101, 102, 137, 138]
# branches []

import pytest
import re
from ansible.module_utils.compat.version import StrictVersion

RE_FLAGS = re.VERBOSE | re.ASCII

def test_strict_version_valid_versions():
    # Test valid versions
    assert StrictVersion.version_re.match("0.4")
    assert StrictVersion.version_re.match("0.4.0")
    assert StrictVersion.version_re.match("0.4.1")
    assert StrictVersion.version_re.match("0.5a1")
    assert StrictVersion.version_re.match("0.5b3")
    assert StrictVersion.version_re.match("0.5")
    assert StrictVersion.version_re.match("0.9.6")
    assert StrictVersion.version_re.match("1.0")
    assert StrictVersion.version_re.match("1.0.4a3")
    assert StrictVersion.version_re.match("1.0.4b1")
    assert StrictVersion.version_re.match("1.0.4")

def test_strict_version_invalid_versions():
    # Test invalid versions
    assert not StrictVersion.version_re.match("1")
    assert not StrictVersion.version_re.match("2.7.2.2")
    assert not StrictVersion.version_re.match("1.3.a4")
    assert not StrictVersion.version_re.match("1.3pl1")
    assert not StrictVersion.version_re.match("1.3c4")
