# file isort/exceptions.py:171-180
# lines [171, 172, 174, 175, 176]
# branches []

import pytest

from isort.exceptions import MissingSection


def test_missing_section_exception():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module="my_module", section="MY_SECTION")

    assert str(exc_info.value) == (
        "Found my_module import while parsing, but MY_SECTION was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
