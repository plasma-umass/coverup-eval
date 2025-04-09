# file flutils/packages.py:169-292
# lines [169, 171, 172, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 244, 246, 247, 248, 249, 250, 251, 254, 255, 257, 258, 259, 260, 261, 262, 265, 266, 267, 268, 271, 272, 273, 274, 275, 278, 280, 281, 283, 284, 285, 286, 289, 290, 291, 292]
# branches ['228->229', '228->230', '230->231', '230->257', '231->232', '231->237', '232->233', '232->235', '237->238', '237->246', '238->239', '238->244', '246->247', '246->248', '248->249', '248->254', '257->258', '257->271', '258->259', '258->265', '271->272', '271->280', '272->273', '272->278', '280->281', '280->283', '283->284', '283->289']

import pytest
from flutils.packages import bump_version

def test_bump_version_major_to_pre_release():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='a')

def test_bump_version_invalid_pre_release():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')

def test_bump_version_position_out_of_bounds():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=3)

def test_bump_version_invalid_version_string():
    with pytest.raises(ValueError):
        bump_version('invalid.version')

def test_bump_version_minor_with_alpha_to_beta():
    assert bump_version('1.2.3a1', pre_release='b') == '1.2.3b0'

def test_bump_version_minor_with_beta_increment():
    assert bump_version('1.2.3b1', pre_release='b') == '1.2.3b2'

def test_bump_version_patch_with_alpha_to_beta():
    assert bump_version('1.2.3a1', position=2, pre_release='b') == '1.2.3b0'

def test_bump_version_patch_with_beta_increment():
    assert bump_version('1.2.3b1', position=2, pre_release='b') == '1.2.3b2'
