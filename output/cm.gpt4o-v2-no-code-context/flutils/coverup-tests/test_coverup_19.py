# file: flutils/packages.py:53-87
# asked: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}
# gained: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}

import pytest
from flutils.packages import _each_version_part
from distutils.version import StrictVersion

def test_each_version_part_no_prerelease():
    ver_obj = StrictVersion("1.2.3")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].txt == '1'
    assert parts[1].txt == '2'
    assert parts[2].txt == '3'

def test_each_version_part_with_prerelease():
    ver_obj = StrictVersion("1.2.0a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].txt == '1'
    assert parts[1].txt == '2a1'
    assert parts[2].txt == ''

def test_each_version_part_with_prerelease_non_zero_patch():
    ver_obj = StrictVersion("1.2.3a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].txt == '1'
    assert parts[1].txt == '2'
    assert parts[2].txt == '3a1'

def test_each_version_part_zero_patch():
    ver_obj = StrictVersion("1.2.0")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].txt == '1'
    assert parts[1].txt == '2'
    assert parts[2].txt == ''

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
