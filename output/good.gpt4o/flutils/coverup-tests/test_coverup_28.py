# file flutils/packages.py:169-292
# lines [169, 171, 172, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 244, 246, 247, 248, 249, 250, 251, 254, 255, 257, 258, 259, 260, 261, 262, 265, 266, 267, 268, 271, 272, 273, 274, 275, 278, 280, 281, 283, 284, 285, 286, 289, 290, 291, 292]
# branches ['228->229', '228->230', '230->231', '230->257', '231->232', '231->237', '232->233', '232->235', '237->238', '237->246', '238->239', '238->244', '246->247', '246->248', '248->249', '248->254', '257->258', '257->271', '258->259', '258->265', '271->272', '271->280', '272->273', '272->278', '280->281', '280->283', '283->284', '283->289']

import pytest
from flutils.packages import bump_version

def test_bump_version():
    # Test bumping the patch version
    assert bump_version('1.2.2') == '1.2.3'
    
    # Test bumping the minor version
    assert bump_version('1.2.3', position=1) == '1.3'
    
    # Test bumping the major version
    assert bump_version('1.3.4', position=0) == '2.0'
    
    # Test bumping to alpha pre-release
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    
    # Test bumping alpha pre-release version
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    
    # Test bumping from alpha to beta pre-release
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    
    # Test bumping from alpha pre-release to final version
    assert bump_version('1.2.4a1') == '1.2.4'
    
    # Test bumping from beta pre-release to final version
    assert bump_version('1.2.4b0') == '1.2.4'
    
    # Test bumping minor version with alpha pre-release
    assert bump_version('2.1.3', position=1, pre_release='a') == '2.2a0'
    
    # Test bumping patch version with beta pre-release
    assert bump_version('1.2b0', position=2) == '1.2.1'
    
    # Test invalid version number
    with pytest.raises(ValueError):
        bump_version('invalid.version')
    
    # Test invalid position
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=5)
    
    # Test invalid pre-release
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')
    
    # Test major version bump to pre-release
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='a')
