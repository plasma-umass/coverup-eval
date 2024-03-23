# file cookiecutter/exceptions.py:69-74
# lines [69, 70]
# branches []

import pytest
from cookiecutter.exceptions import VCSNotInstalled

def test_vcs_not_installed_exception():
    with pytest.raises(VCSNotInstalled) as exc_info:
        raise VCSNotInstalled("Test VCS not installed exception.")

    assert str(exc_info.value) == "Test VCS not installed exception."
