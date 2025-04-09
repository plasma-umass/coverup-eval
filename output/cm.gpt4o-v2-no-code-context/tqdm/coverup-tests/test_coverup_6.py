# file: tqdm/notebook.py:255-263
# asked: {"lines": [255, 256, 257, 259, 261, 262, 263], "branches": [[257, 0], [257, 259]]}
# gained: {"lines": [255, 256, 257, 259, 261, 262, 263], "branches": [[257, 0], [257, 259]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming tqdm_notebook is imported from tqdm.notebook
from tqdm.notebook import tqdm_notebook

class TestTqdmNotebook:
    @pytest.fixture
    def mock_super_iter(self, monkeypatch):
        mock_iter = MagicMock()
        monkeypatch.setattr('tqdm.notebook.std_tqdm.__iter__', mock_iter)
        return mock_iter

    def test_tqdm_notebook_iter_success(self, mock_super_iter):
        # Mock the super iterator to return a list of items
        mock_super_iter.return_value = iter([1, 2, 3])
        
        # Create an instance of tqdm_notebook
        tqdm_instance = tqdm_notebook()
        
        # Collect the items from the iterator
        items = list(tqdm_instance)
        
        # Assert that the items are as expected
        assert items == [1, 2, 3]
        
        # Assert that the super iterator was called
        mock_super_iter.assert_called_once()

    def test_tqdm_notebook_iter_exception(self, mock_super_iter):
        # Mock the super iterator to raise an exception
        mock_super_iter.side_effect = Exception("Test Exception")
        
        # Create an instance of tqdm_notebook
        tqdm_instance = tqdm_notebook()
        
        # Patch the disp method to check if it is called with the correct argument
        with patch.object(tqdm_instance, 'disp', autospec=True) as mock_disp:
            with pytest.raises(Exception, match="Test Exception"):
                list(tqdm_instance)
            
            # Assert that disp was called with the correct argument
            mock_disp.assert_called_once_with(bar_style='danger')
