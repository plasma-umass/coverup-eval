# file: tqdm/gui.py:181-186
# asked: {"lines": [181, 186], "branches": []}
# gained: {"lines": [181, 186], "branches": []}

import pytest
from tqdm.gui import tqdm_gui

def test_tgrange(monkeypatch):
    from tqdm.gui import tgrange

    # Mock tqdm_gui to verify it is called with the correct arguments
    def mock_tqdm_gui(iterable, **kwargs):
        assert list(iterable) == list(range(5))
        assert kwargs == {'desc': 'test'}
        return "mocked"

    monkeypatch.setattr('tqdm.gui.tqdm_gui', mock_tqdm_gui)

    result = tgrange(5, desc='test')
    assert result == "mocked"
