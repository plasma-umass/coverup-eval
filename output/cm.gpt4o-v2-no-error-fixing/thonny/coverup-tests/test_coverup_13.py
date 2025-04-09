# file: thonny/jedi_utils.py:123-131
# asked: {"lines": [123, 124, 126, 127, 128, 130, 131], "branches": [[126, 127], [126, 130]]}
# gained: {"lines": [123, 124, 126, 127, 128, 130, 131], "branches": [[126, 127], [126, 130]]}

import pytest
from unittest import mock
import jedi
from thonny.jedi_utils import get_definitions

def test_get_definitions_with_older_jedi(monkeypatch):
    source = "def foo(): pass"
    row = 1
    column = 1
    filename = "test.py"

    def mock_using_older_jedi(jedi):
        return True

    monkeypatch.setattr("thonny.jedi_utils._using_older_jedi", mock_using_older_jedi)

    mock_script = mock.Mock()
    mock_script.goto_definitions.return_value = ["definition"]

    with mock.patch("jedi.Script", return_value=mock_script) as mock_jedi_script:
        result = get_definitions(source, row, column, filename)
        mock_jedi_script.assert_called_once_with(source, row, column, filename)
        assert result == ["definition"]

def test_get_definitions_with_newer_jedi(monkeypatch):
    source = "def foo(): pass"
    row = 1
    column = 1
    filename = "test.py"

    def mock_using_older_jedi(jedi):
        return False

    monkeypatch.setattr("thonny.jedi_utils._using_older_jedi", mock_using_older_jedi)

    mock_script = mock.Mock()
    mock_script.infer.return_value = ["inference"]

    with mock.patch("jedi.Script", return_value=mock_script) as mock_jedi_script:
        result = get_definitions(source, row, column, filename)
        mock_jedi_script.assert_called_once_with(code=source, path=filename)
        assert result == ["inference"]
