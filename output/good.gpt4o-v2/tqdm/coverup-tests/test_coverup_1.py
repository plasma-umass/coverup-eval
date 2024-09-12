# file: tqdm/gui.py:181-186
# asked: {"lines": [181, 186], "branches": []}
# gained: {"lines": [181, 186], "branches": []}

import pytest
from tqdm.gui import tgrange
from tqdm.gui import tqdm_gui
from unittest.mock import patch

@pytest.mark.parametrize("args, kwargs", [
    ((10,), {}),
    ((5, 15), {'colour': 'r'}),
    ((0, 20, 2), {'disable': True}),
])
def test_tgrange(args, kwargs):
    with patch('tqdm.gui.tqdm_gui') as mock_tqdm_gui:
        tgrange(*args, **kwargs)
        mock_tqdm_gui.assert_called_once_with(range(*args), **kwargs)
