# file: src/blib2to3/pgen2/grammar.py:119-123
# asked: {"lines": [119, 121, 122, 123], "branches": []}
# gained: {"lines": [119, 121, 122, 123], "branches": []}

import pytest
import pickle
from pathlib import Path
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def temp_pickle_file(tmp_path):
    data = {'key': 'value'}
    file_path = tmp_path / "test_grammar.pkl"
    with open(file_path, "wb") as f:
        pickle.dump(data, f)
    yield file_path
    file_path.unlink()

def test_load_method_executes_all_lines(temp_pickle_file, mocker):
    grammar = Grammar()
    mock_update = mocker.patch.object(grammar, '_update', autospec=True)
    
    grammar.load(temp_pickle_file)
    
    mock_update.assert_called_once()
    assert mock_update.call_args[0][0] == {'key': 'value'}
