# file: thonny/jedi_utils.py:123-131
# asked: {"lines": [124, 126, 127, 128, 130, 131], "branches": [[126, 127], [126, 130]]}
# gained: {"lines": [124, 126, 127, 128, 130, 131], "branches": [[126, 127], [126, 130]]}

import pytest
import jedi
from thonny.jedi_utils import get_definitions

def test_get_definitions_old_jedi(monkeypatch):
    class MockScript:
        def __init__(self, source, row, column, filename):
            self.source = source
            self.row = row
            self.column = column
            self.filename = filename

        def goto_definitions(self):
            return ["definition1", "definition2"]

    def mock_using_older_jedi(jedi_module):
        return True

    monkeypatch.setattr('thonny.jedi_utils._using_older_jedi', mock_using_older_jedi)
    monkeypatch.setattr('jedi.Script', MockScript)

    source = "def foo(): pass"
    row = 1
    column = 4
    filename = "test.py"
    definitions = get_definitions(source, row, column, filename)
    assert definitions == ["definition1", "definition2"]

def test_get_definitions_new_jedi(monkeypatch):
    class MockScript:
        def __init__(self, code, path):
            self.code = code
            self.path = path

        def infer(self, line, column):
            return ["inference1", "inference2"]

    def mock_using_older_jedi(jedi_module):
        return False

    monkeypatch.setattr('thonny.jedi_utils._using_older_jedi', mock_using_older_jedi)
    monkeypatch.setattr('jedi.Script', MockScript)

    source = "def foo(): pass"
    row = 1
    column = 4
    filename = "test.py"
    definitions = get_definitions(source, row, column, filename)
    assert definitions == ["inference1", "inference2"]
