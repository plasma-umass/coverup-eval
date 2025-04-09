# file: isort/exceptions.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import pytest
from isort.exceptions import ISortError, FormattingPluginDoesNotExist

def test_formatting_plugin_does_not_exist():
    formatter_name = "non_existent_formatter"
    exception = FormattingPluginDoesNotExist(formatter_name)
    
    assert isinstance(exception, ISortError)
    assert str(exception) == f"Specified formatting plugin of {formatter_name} does not exist. "
    assert exception.formatter == formatter_name
