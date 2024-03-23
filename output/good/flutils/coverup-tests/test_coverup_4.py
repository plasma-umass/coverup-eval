# file flutils/packages.py:44-50
# lines [44, 45, 46, 47, 48, 49, 50]
# branches []

import pytest
from flutils.packages import _VersionPart

def test_version_part_namedtuple():
    # Create an instance of _VersionPart with all fields
    version_part = _VersionPart(
        pos=1,
        txt='1.0.0',
        num=100,
        pre_txt='alpha',
        pre_num=1,
        name='test'
    )

    # Assert that all fields are correctly set
    assert version_part.pos == 1
    assert version_part.txt == '1.0.0'
    assert version_part.num == 100
    assert version_part.pre_txt == 'alpha'
    assert version_part.pre_num == 1
    assert version_part.name == 'test'

    # Assert that the namedtuple is correctly typed
    assert isinstance(version_part, _VersionPart)

    # Assert that the namedtuple is immutable
    with pytest.raises(AttributeError):
        version_part.pos = 2
