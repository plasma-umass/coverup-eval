# file: flutils/packages.py:130-166
# asked: {"lines": [130, 134, 135, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164], "branches": [[134, 135], [134, 137], [140, 141], [140, 146], [141, 142], [141, 143], [143, 144], [143, 145], [146, 147], [146, 163], [148, 149], [148, 151], [151, 152], [151, 156], [156, 157], [156, 160], [157, 158], [157, 159], [160, 161], [160, 162]]}
# gained: {"lines": [130, 134, 135, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164], "branches": [[134, 135], [134, 137], [140, 141], [140, 146], [141, 142], [141, 143], [143, 144], [143, 145], [146, 147], [146, 163], [148, 149], [148, 151], [151, 152], [151, 156], [156, 157], [156, 160], [157, 158], [157, 159], [160, 161], [160, 162]]}

import pytest
from flutils.packages import _build_version_bump_type

_BUMP_VERSION_MAJOR = 0
_BUMP_VERSION_MINOR = 1
_BUMP_VERSION_PATCH = 2
_BUMP_VERSION_MINOR_ALPHA = 3
_BUMP_VERSION_MINOR_BETA = 4
_BUMP_VERSION_PATCH_ALPHA = 5
_BUMP_VERSION_PATCH_BETA = 6

def test_build_version_bump_type_no_prerelease_major():
    assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR

def test_build_version_bump_type_no_prerelease_minor():
    assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR

def test_build_version_bump_type_no_prerelease_patch():
    assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH

def test_build_version_bump_type_alpha_minor():
    assert _build_version_bump_type(1, 'alpha') == _BUMP_VERSION_MINOR_ALPHA

def test_build_version_bump_type_alpha_patch():
    assert _build_version_bump_type(2, 'alpha') == _BUMP_VERSION_PATCH_ALPHA

def test_build_version_bump_type_beta_minor():
    assert _build_version_bump_type(1, 'beta') == _BUMP_VERSION_MINOR_BETA

def test_build_version_bump_type_beta_patch():
    assert _build_version_bump_type(2, 'beta') == _BUMP_VERSION_PATCH_BETA

def test_build_version_bump_type_invalid_prerelease():
    with pytest.raises(ValueError, match="The given value for 'pre_release'"):
        _build_version_bump_type(1, 'invalid')

def test_build_version_bump_type_prerelease_major():
    with pytest.raises(ValueError, match="Only the 'minor' or 'patch' parts of the version number"):
        _build_version_bump_type(0, 'alpha')
