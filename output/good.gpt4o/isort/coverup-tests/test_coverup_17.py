# file isort/exceptions.py:171-180
# lines [171, 172, 174, 175, 176]
# branches []

import pytest
from isort.exceptions import MissingSection

def test_missing_section():
    import_module = "example_module"
    section = "example_section"
    
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module, section)
    
    assert str(exc_info.value) == (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
