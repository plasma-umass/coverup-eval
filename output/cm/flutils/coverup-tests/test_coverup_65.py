# file flutils/packages.py:169-292
# lines [229, 231, 232, 233, 235, 237, 238, 239, 240, 241, 244, 246, 247, 248, 249, 250, 251, 254, 255, 258, 259, 260, 261, 262, 265, 266, 267, 268, 272, 273, 274, 275, 278, 289]
# branches ['228->229', '230->231', '231->232', '231->237', '232->233', '232->235', '237->238', '237->246', '238->239', '238->244', '246->247', '246->248', '248->249', '248->254', '257->258', '258->259', '258->265', '271->272', '272->273', '272->278', '283->289']

import pytest
from flutils.packages import bump_version

def test_bump_version_coverage():
    # Test bumping major version
    assert bump_version('1.2.3', position=0) == '2.0'
    
    # Test bumping minor version without pre-release
    assert bump_version('1.2.3', position=1) == '1.3'
    
    # Test bumping minor version with alpha pre-release
    assert bump_version('1.2.3', position=1, pre_release='a') == '1.3a0'
    
    # Test bumping minor version with beta pre-release
    assert bump_version('1.2.3', position=1, pre_release='b') == '1.3b0'
    
    # Test bumping minor version with alpha pre-release when already alpha
    assert bump_version('1.2.3a1', pre_release='a') == '1.2.3a2'
    
    # Test bumping minor version with beta pre-release when already alpha
    assert bump_version('1.2.3a1', pre_release='b') == '1.2.3b0'
    
    # Test bumping minor version with beta pre-release when already beta
    assert bump_version('1.2.3b1', pre_release='b') == '1.2.3b2'
    
    # Test bumping patch version without pre-release
    assert bump_version('1.2.3', position=2) == '1.2.4'
    
    # Test bumping patch version with alpha pre-release
    assert bump_version('1.2.3', position=2, pre_release='a') == '1.2.4a0'
    
    # Test bumping patch version with beta pre-release
    assert bump_version('1.2.3', position=2, pre_release='b') == '1.2.4b0'
    
    # Test bumping patch version with alpha pre-release when already alpha
    assert bump_version('1.2.3a1', position=2, pre_release='a') == '1.2.3a2'
    
    # Test bumping patch version with beta pre-release when already alpha
    assert bump_version('1.2.3a1', position=2, pre_release='b') == '1.2.3b0'
    
    # Test bumping patch version with beta pre-release when already beta
    assert bump_version('1.2.3b1', position=2, pre_release='b') == '1.2.3b2'
    
    # Test bumping patch version without pre-release when already alpha
    assert bump_version('1.2.3a1', position=2) == '1.2.3'
    
    # Test bumping patch version without pre-release when already beta
    assert bump_version('1.2.3b1', position=2) == '1.2.3'
    
    # Test bumping minor version without pre-release when already alpha
    assert bump_version('1.2.3a1', position=1) == '1.3'
    
    # Test bumping minor version without pre-release when already beta
    assert bump_version('1.2.3b1', position=1) == '1.3'
    
    # Test bumping major version with pre-release should raise ValueError
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='a')
    
    # Test bumping with invalid pre-release should raise ValueError
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')
    
    # Test bumping with invalid position should raise ValueError
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=3)
    
    # Test bumping with invalid version should raise ValueError
    with pytest.raises(ValueError):
        bump_version('invalid_version')
