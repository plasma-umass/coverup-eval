# file: isort/exceptions.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_formatting_plugin_does_not_exist():
    formatter_name = "non_existent_formatter"
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter_name)
    
    assert str(exc_info.value) == f"Specified formatting plugin of {formatter_name} does not exist. "
    assert exc_info.value.formatter == formatter_name
