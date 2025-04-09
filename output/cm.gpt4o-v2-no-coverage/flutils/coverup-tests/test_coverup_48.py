# file: flutils/packages.py:130-166
# asked: {"lines": [130, 134, 135, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164], "branches": [[134, 135], [134, 137], [140, 141], [140, 146], [141, 142], [141, 143], [143, 144], [143, 145], [146, 147], [146, 163], [148, 149], [148, 151], [151, 152], [151, 156], [156, 157], [156, 160], [157, 158], [157, 159], [160, 161], [160, 162]]}
# gained: {"lines": [130, 134, 135, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 156, 157, 158, 159, 160, 161, 162, 163, 164], "branches": [[134, 135], [134, 137], [140, 141], [140, 146], [141, 142], [141, 143], [143, 144], [143, 145], [146, 147], [146, 163], [148, 149], [148, 151], [151, 152], [151, 156], [156, 157], [156, 160], [157, 158], [157, 159], [160, 161], [160, 162]]}

import pytest
from flutils.packages import _build_version_bump_type

# Constants for testing
_BUMP_VERSION_MAJOR = 1
_BUMP_VERSION_MINOR = 2
_BUMP_VERSION_PATCH = 3
_BUMP_VERSION_MINOR_ALPHA = 4
_BUMP_VERSION_MINOR_BETA = 5
_BUMP_VERSION_PATCH_ALPHA = 6
_BUMP_VERSION_PATCH_BETA = 7

def test_build_version_bump_type_no_prerelease(monkeypatch):
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_MAJOR', _BUMP_VERSION_MAJOR)
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_MINOR', _BUMP_VERSION_MINOR)
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_PATCH', _BUMP_VERSION_PATCH)
    assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR
    assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR
    assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH

def test_build_version_bump_type_alpha_prerelease(monkeypatch):
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_MINOR_ALPHA', _BUMP_VERSION_MINOR_ALPHA)
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_PATCH_ALPHA', _BUMP_VERSION_PATCH_ALPHA)
    assert _build_version_bump_type(1, 'a') == _BUMP_VERSION_MINOR_ALPHA
    assert _build_version_bump_type(1, 'alpha') == _BUMP_VERSION_MINOR_ALPHA
    assert _build_version_bump_type(2, 'a') == _BUMP_VERSION_PATCH_ALPHA
    assert _build_version_bump_type(2, 'alpha') == _BUMP_VERSION_PATCH_ALPHA

def test_build_version_bump_type_beta_prerelease(monkeypatch):
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_MINOR_BETA', _BUMP_VERSION_MINOR_BETA)
    monkeypatch.setattr('flutils.packages._BUMP_VERSION_PATCH_BETA', _BUMP_VERSION_PATCH_BETA)
    assert _build_version_bump_type(1, 'b') == _BUMP_VERSION_MINOR_BETA
    assert _build_version_bump_type(1, 'beta') == _BUMP_VERSION_MINOR_BETA
    assert _build_version_bump_type(2, 'b') == _BUMP_VERSION_PATCH_BETA
    assert _build_version_bump_type(2, 'beta') == _BUMP_VERSION_PATCH_BETA

def test_build_version_bump_type_invalid_prerelease():
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'a')
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'alpha')
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'b')
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'beta')
    with pytest.raises(ValueError):
        _build_version_bump_type(1, 'invalid')
    with pytest.raises(ValueError):
        _build_version_bump_type(2, 'invalid')
