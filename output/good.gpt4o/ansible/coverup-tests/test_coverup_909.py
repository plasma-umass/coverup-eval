# file lib/ansible/modules/apt_repository.py:189-190
# lines [189, 190]
# branches []

import pytest
from ansible.modules.apt_repository import InvalidSource

def test_invalid_source_exception():
    with pytest.raises(InvalidSource):
        raise InvalidSource("This is a test exception")

# Ensure the test cleans up properly
def test_cleanup(mocker):
    mocker.patch('ansible.modules.apt_repository.InvalidSource', side_effect=InvalidSource)
    try:
        raise InvalidSource("This is a test exception")
    except InvalidSource:
        pass
    finally:
        mocker.stopall()
