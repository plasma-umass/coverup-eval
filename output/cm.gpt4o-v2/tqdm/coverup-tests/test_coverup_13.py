# file: tqdm/rich.py:142-147
# asked: {"lines": [142, 147], "branches": []}
# gained: {"lines": [142, 147], "branches": []}

import pytest
from tqdm.rich import trrange
from tqdm.rich import tqdm_rich

def test_trrange(monkeypatch):
    # Mock tqdm_rich to ensure it is called with expected arguments
    def mock_tqdm_rich(*args, **kwargs):
        assert args == (range(10),)
        assert kwargs == {'foo': 'bar'}
        return "mocked"

    monkeypatch.setattr('tqdm.rich.tqdm_rich', mock_tqdm_rich)

    result = trrange(10, foo='bar')
    assert result == "mocked"
