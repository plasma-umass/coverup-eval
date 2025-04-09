# file flutils/packages.py:130-166
# lines [130, 134, 135, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164]
# branches ['134->135', '134->137', '140->141', '140->146', '141->142', '141->143', '143->144', '143->145', '146->147', '146->163', '148->149', '148->151', '151->152', '151->156', '156->157', '156->160', '157->158', '157->159', '160->161', '160->162']

import pytest
from flutils.packages import _build_version_bump_type

# Assuming these constants are defined in the flutils.packages module
# and are imported here for testing purposes.
from flutils.packages import (
    _BUMP_VERSION_MAJOR,
    _BUMP_VERSION_MINOR,
    _BUMP_VERSION_PATCH,
    _BUMP_VERSION_MINOR_ALPHA,
    _BUMP_VERSION_MINOR_BETA,
    _BUMP_VERSION_PATCH_ALPHA,
    _BUMP_VERSION_PATCH_BETA
)

def test_build_version_bump_type_major():
    assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR

def test_build_version_bump_type_minor():
    assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR

def test_build_version_bump_type_patch():
    assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH

def test_build_version_bump_type_minor_alpha():
    assert _build_version_bump_type(1, 'alpha') == _BUMP_VERSION_MINOR_ALPHA

def test_build_version_bump_type_minor_beta():
    assert _build_version_bump_type(1, 'beta') == _BUMP_VERSION_MINOR_BETA

def test_build_version_bump_type_patch_alpha():
    assert _build_version_bump_type(2, 'a') == _BUMP_VERSION_PATCH_ALPHA

def test_build_version_bump_type_patch_beta():
    assert _build_version_bump_type(2, 'b') == _BUMP_VERSION_PATCH_BETA

def test_build_version_bump_type_invalid_pre_release():
    with pytest.raises(ValueError) as excinfo:
        _build_version_bump_type(1, 'invalid')
    assert "The given value for 'pre_release'" in str(excinfo.value)

def test_build_version_bump_type_major_with_pre_release():
    with pytest.raises(ValueError) as excinfo:
        _build_version_bump_type(0, 'alpha')
    assert "Only the 'minor' or 'patch' parts of the version number" in str(excinfo.value)
