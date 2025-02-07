# file: flutils/packages.py:169-292
# asked: {"lines": [169, 171, 172, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 244, 246, 247, 248, 249, 250, 251, 254, 255, 257, 258, 259, 260, 261, 262, 265, 266, 267, 268, 271, 272, 273, 274, 275, 278, 280, 281, 283, 284, 285, 286, 289, 290, 291, 292], "branches": [[228, 229], [228, 230], [230, 231], [230, 257], [231, 232], [231, 237], [232, 233], [232, 235], [237, 238], [237, 246], [238, 239], [238, 244], [246, 247], [246, 248], [248, 249], [248, 254], [257, 258], [257, 271], [258, 259], [258, 265], [271, 272], [271, 280], [272, 273], [272, 278], [280, 281], [280, 283], [283, 284], [283, 289]]}
# gained: {"lines": [169, 171, 172, 223, 224, 225, 227, 228, 229, 230, 231, 232, 235, 237, 238, 244, 246, 248, 254, 255, 257, 258, 265, 266, 267, 268, 271, 272, 273, 274, 275, 278, 280, 281, 283, 284, 285, 286, 290, 291, 292], "branches": [[228, 229], [228, 230], [230, 231], [230, 257], [231, 232], [231, 237], [232, 235], [237, 238], [237, 246], [238, 244], [246, 248], [248, 254], [257, 258], [257, 271], [258, 265], [271, 272], [271, 280], [272, 273], [272, 278], [280, 281], [280, 283], [283, 284]]}

import pytest
from flutils.packages import bump_version

def test_bump_version_patch():
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.9') == '1.2.10'

def test_bump_version_minor():
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.9.3', position=1) == '1.10'

def test_bump_version_major():
    assert bump_version('1.2.3', position=0) == '2.0'
    assert bump_version('9.2.3', position=0) == '10.0'

def test_bump_version_alpha():
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

def test_bump_version_beta():
    assert bump_version('1.2.4b0', pre_release='b') == '1.2.4b1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

def test_bump_version_minor_alpha():
    assert bump_version('2.1.3', position=1, pre_release='a') == '2.2a0'
    assert bump_version('2.1.3a0', position=2, pre_release='a') == '2.1.3a1'

def test_bump_version_minor_beta():
    assert bump_version('2.1.3', position=1, pre_release='b') == '2.2b0'
    assert bump_version('2.1.3b0', position=2, pre_release='b') == '2.1.3b1'

def test_bump_version_patch_alpha():
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

def test_bump_version_patch_beta():
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4b0', pre_release='b') == '1.2.4b1'

def test_bump_version_invalid_version():
    with pytest.raises(ValueError):
        bump_version('invalid.version')

def test_bump_version_invalid_position():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=10)

def test_bump_version_invalid_prerelease():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')

def test_bump_version_major_prerelease():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='a')
