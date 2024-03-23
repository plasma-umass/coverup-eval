# file cookiecutter/exceptions.py:21-27
# lines [21, 22]
# branches []

import pytest
from cookiecutter.exceptions import UnknownTemplateDirException

def test_unknown_template_dir_exception():
    with pytest.raises(UnknownTemplateDirException) as exc_info:
        raise UnknownTemplateDirException("Ambiguous project template directory.")

    assert str(exc_info.value) == "Ambiguous project template directory."
