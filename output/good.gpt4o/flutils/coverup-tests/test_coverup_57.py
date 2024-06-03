# file flutils/packages.py:130-166
# lines [159]
# branches ['157->159']

import pytest
from flutils.packages import _build_version_bump_type

_BUMP_VERSION_MAJOR = 0
_BUMP_VERSION_MINOR = 1
_BUMP_VERSION_PATCH = 2
_BUMP_VERSION_MINOR_ALPHA = 3
_BUMP_VERSION_MINOR_BETA = 4
_BUMP_VERSION_PATCH_ALPHA = 5
_BUMP_VERSION_PATCH_BETA = 6

def test_build_version_bump_type_minor_beta():
    position_positive = 1
    pre_release = 'beta'
    result = _build_version_bump_type(position_positive, pre_release)
    assert result == _BUMP_VERSION_MINOR_BETA

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here

