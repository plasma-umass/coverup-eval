# file: cookiecutter/exceptions.py:69-74
# asked: {"lines": [69, 70], "branches": []}
# gained: {"lines": [69, 70], "branches": []}

import pytest
from cookiecutter.exceptions import VCSNotInstalled

def test_vcs_not_installed_exception():
    with pytest.raises(VCSNotInstalled) as exc_info:
        raise VCSNotInstalled("Version control system is not installed.")
    assert str(exc_info.value) == "Version control system is not installed."
