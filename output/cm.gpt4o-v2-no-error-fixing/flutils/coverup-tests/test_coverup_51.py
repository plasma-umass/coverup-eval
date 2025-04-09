# file: flutils/packages.py:130-166
# asked: {"lines": [159], "branches": [[157, 159]]}
# gained: {"lines": [159], "branches": [[157, 159]]}

import pytest

# Assuming the constants are defined somewhere in the module
_BUMP_VERSION_MAJOR = 0
_BUMP_VERSION_MINOR = 1
_BUMP_VERSION_PATCH = 2
_BUMP_VERSION_MINOR_ALPHA = 3
_BUMP_VERSION_MINOR_BETA = 4
_BUMP_VERSION_PATCH_ALPHA = 5
_BUMP_VERSION_PATCH_BETA = 6

from flutils.packages import _build_version_bump_type

def test_build_version_bump_type_minor_beta():
    result = _build_version_bump_type(1, 'beta')
    assert result == _BUMP_VERSION_MINOR_BETA

def test_build_version_bump_type_minor_beta_uppercase():
    result = _build_version_bump_type(1, 'BETA')
    assert result == _BUMP_VERSION_MINOR_BETA

def test_build_version_bump_type_minor_beta_with_spaces():
    result = _build_version_bump_type(1, '  beta  ')
    assert result == _BUMP_VERSION_MINOR_BETA
